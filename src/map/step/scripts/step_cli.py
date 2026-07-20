#!/usr/bin/env python3
"""Lightweight helper for STEP-<slug>.yaml files.

Command shape: step_cli.py <operation> <resource> [--field value]
Patch commands are escape hatches; prefer explicit update/append commands.

Exit codes:
  0 success
  1 usage/argument error
  2 lint failure
  3 file/env error
  4 YAML parse or schema-shape error during an operation

Self-test:
  step_cli.py --test

Preview:
  step_cli.py --dry-run <mutating operation>
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only when dependency is absent.
    yaml = None  # type: ignore[assignment]

log = logging.getLogger(__name__)

EXIT_OK = 0
EXIT_USAGE = 1
EXIT_LINT = 2
EXIT_FILE = 3
EXIT_SCHEMA = 4

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STEP_FIELD_ORDER = ["slug", "intent", "do", "validate", "retro", "next_steps", "recommendation"]
TOP_FIELD_ORDER = ["goal", "lessons", "steps"]


class StepCliError(Exception):
    def __init__(self, message: str, code: int = EXIT_SCHEMA) -> None:
        super().__init__(message)
        self.code = code


class StepArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        self.print_usage(sys.stderr)
        raise StepCliError(message, EXIT_USAGE)


def warn(message: str) -> None:
    log.warning(message)


def emit(obj: Any) -> None:
    print(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), end="")


def normalize_match(value: str) -> str:
    lowered = value.lower()
    return "".join(ch for ch in lowered if not unicodedata.category(ch).startswith("P"))


def dedupe_normalized(values: list[Any]) -> tuple[list[str], bool]:
    seen: set[str] = set()
    out: list[str] = []
    changed = False
    for item in values:
        text = str(item)
        key = normalize_match(text)
        if key in seen:
            changed = True
            continue
        seen.add(key)
        out.append(text)
    return out, changed


def dedupe_slugs(values: list[Any]) -> tuple[list[str], bool]:
    seen: set[str] = set()
    out: list[str] = []
    changed = False
    for item in values:
        text = str(item).strip()
        if text in seen:
            changed = True
            continue
        seen.add(text)
        out.append(text)
    return out, changed


def parse_yaml_value(value: str) -> Any:
    raw = sys.stdin.read() if value == "-" else value
    try:
        return yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        raise StepCliError(f"failed to parse YAML value: {exc}", EXIT_SCHEMA) from exc


def ensure_mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise StepCliError(f"{name} must be a YAML mapping/object")
    return value


def ensure_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise StepCliError(f"{name} must be a YAML list")
    return value


def resolve_file(args: argparse.Namespace, *, for_init: bool = False) -> Path:
    file_value = args.file or os.environ.get("STEP_FILE")
    if not file_value:
        raise StepCliError("provide --file STEP-<slug>.yaml or set STEP_FILE", EXIT_FILE)
    path = Path(file_value)
    if not for_init and not path.exists():
        raise StepCliError(f"step file does not exist: {path}", EXIT_FILE)
    return path


def read_step_file(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text())
    except OSError as exc:
        raise StepCliError(f"failed to read {path}: {exc}", EXIT_FILE) from exc
    except yaml.YAMLError as exc:
        raise StepCliError(f"failed to parse {path}: {exc}", EXIT_SCHEMA) from exc
    if not isinstance(data, dict):
        raise StepCliError("step file must contain a top-level mapping")
    return data


def ordered_step(step: dict[str, Any]) -> dict[str, Any]:
    ordered: dict[str, Any] = {}
    for key in STEP_FIELD_ORDER:
        if key in step:
            ordered[key] = step[key]
    for key, value in step.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def normalize_document(data: dict[str, Any]) -> dict[str, Any]:
    if isinstance(data.get("lessons"), list):
        data["lessons"], _ = dedupe_normalized(data["lessons"])
    if isinstance(data.get("steps"), list):
        for i, step in enumerate(data["steps"]):
            if not isinstance(step, dict):
                continue
            if isinstance(step.get("next_steps"), list):
                step["next_steps"], _ = dedupe_slugs(step["next_steps"])
            retro = step.get("retro")
            if isinstance(retro, dict):
                for key in ("wins", "issues", "actions"):
                    if isinstance(retro.get(key), list):
                        retro[key], _ = dedupe_normalized(retro[key])
            data["steps"][i] = ordered_step(step)
    ordered: dict[str, Any] = {}
    for key in TOP_FIELD_ORDER:
        if key in data:
            ordered[key] = data[key]
    for key, value in data.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def write_step_file(
    path: Path,
    data: dict[str, Any],
    *,
    create_parent: bool = False,
    dry_run: bool = False,
) -> None:
    if dry_run:
        normalize_document(data)
        return
    if create_parent:
        path.parent.mkdir(parents=True, exist_ok=True)
    data = normalize_document(data)
    try:
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
    except OSError as exc:
        raise StepCliError(f"failed to write {path}: {exc}", EXIT_FILE) from exc


def last_step(data: dict[str, Any]) -> dict[str, Any]:
    steps = data.get("steps")
    if not isinstance(steps, list) or not steps:
        raise StepCliError("step file has no steps")
    step = steps[-1]
    if not isinstance(step, dict):
        raise StepCliError("last step must be a mapping/object")
    return step


def result(args: argparse.Namespace, changed: bool, **extra: Any) -> dict[str, Any]:
    payload = {
        "ok": True,
        "file": str(resolve_file(args)),
        "operation": args.operation,
        "resource": args.resource,
        "changed": changed,
        "dry_run": args.dry_run,
    }
    payload.update(extra)
    return payload


def command_init(args: argparse.Namespace) -> int:
    path = resolve_file(args, for_init=True)
    if path.exists() and not args.force:
        raise StepCliError(f"step file already exists: {path}; use --force to overwrite", EXIT_FILE)
    lessons, _ = dedupe_normalized(args.lesson or [])
    data = {
        "goal": args.goal,
        "lessons": lessons,
        "steps": [{"slug": args.slug, "intent": args.intent}],
    }
    validate_slug(args.slug, "slug")
    write_step_file(path, data, create_parent=True, dry_run=args.dry_run)
    emit({
        "ok": True,
        "file": str(path),
        "operation": "init",
        "resource": "step",
        "changed": True,
        "dry_run": args.dry_run,
    })
    return EXIT_OK


def command_show(args: argparse.Namespace) -> int:
    data = read_step_file(resolve_file(args))
    resource = args.resource
    if resource == "all":
        emit(normalize_document(data))
    elif resource == "continuation":
        emit({
            "goal": data.get("goal"),
            "lessons": data.get("lessons", []),
            "last_step": last_step(data),
        })
    elif resource == "goal":
        emit({"goal": data.get("goal")})
    elif resource == "lessons":
        emit({"lessons": data.get("lessons", [])})
    elif resource == "last":
        emit({"last_step": last_step(data)})
    else:
        raise StepCliError(f"unsupported show resource: {resource}", EXIT_USAGE)
    return EXIT_OK


def command_update(args: argparse.Namespace) -> int:
    path = resolve_file(args)
    data = read_step_file(path)
    changed = False
    if args.resource == "goal":
        old = data.get("goal")
        data["goal"] = args.value
        changed = old != args.value
    elif args.resource == "last":
        step = last_step(data)
        supplied = [
            ("do", args.do),
            ("validate", args.validate),
            ("next_steps", args.next_steps),
            ("recommendation", args.recommendation),
        ]
        fields = [(name, value) for name, value in supplied if value is not None]
        if len(fields) != 1:
            raise StepCliError(
                "update last requires exactly one of --do, --validate, "
                "--next-steps, or --recommendation",
                EXIT_USAGE,
            )
        field, raw = fields[0]
        value = parse_yaml_value(raw)
        if field in {"do", "validate", "recommendation"}:
            value = ensure_mapping(value, field)
        if field == "next_steps":
            value = coerce_slug_list(value, "next_steps")
            value, _ = dedupe_slugs(value)
            rec = step.get("recommendation")
            if isinstance(rec, dict) and rec.get("next") and rec.get("next") not in value:
                warn(
                    "recommendation.next is not present in updated next_steps; "
                    "lint complete will report this"
                )
        if field == "recommendation":
            rec_next = value.get("next")
            next_steps = step.get("next_steps", [])
            if rec_next and isinstance(next_steps, list) and rec_next not in next_steps:
                warn(
                    "recommendation.next is not present in next_steps; "
                    "lint complete will report this"
                )
        old = step.get(field)
        step[field] = value
        changed = old != value
    else:
        raise StepCliError(f"unsupported update resource: {args.resource}", EXIT_USAGE)
    if changed:
        write_step_file(path, data, dry_run=args.dry_run)
    emit(result(args, changed))
    return EXIT_OK


def command_append(args: argparse.Namespace) -> int:
    path = resolve_file(args)
    data = read_step_file(path)
    changed = False
    if args.resource == "lessons":
        lessons = data.setdefault("lessons", [])
        if not isinstance(lessons, list):
            raise StepCliError("lessons must be a list")
        before = list(lessons)
        lessons.append(args.value)
        data["lessons"], _ = dedupe_normalized(lessons)
        changed = before != data["lessons"]
    elif args.resource == "step":
        validate_slug(args.slug, "slug")
        steps = data.setdefault("steps", [])
        if not isinstance(steps, list):
            raise StepCliError("steps must be a list")
        existing = [s.get("slug") for s in steps if isinstance(s, dict)]
        if args.slug in existing:
            raise StepCliError(f"step slug already exists: {args.slug}")
        if steps:
            prev = last_step(data)
            next_steps = prev.get("next_steps", [])
            if isinstance(next_steps, list) and args.slug not in next_steps:
                warn("new step slug is not listed in previous next_steps")
        steps.append({"slug": args.slug, "intent": args.intent})
        changed = True
    elif args.resource == "last":
        step = last_step(data)
        fields = [("retro", args.retro), ("next_steps", args.next_steps)]
        fields = [(name, value) for name, value in fields if value is not None]
        if len(fields) != 1:
            raise StepCliError(
                "append last requires exactly one of --retro or --next-steps",
                EXIT_USAGE,
            )
        field, raw = fields[0]
        value = parse_yaml_value(raw)
        if field == "retro":
            value = ensure_mapping(value, "retro")
            changed = merge_retro(step, value)
        else:
            values = coerce_slug_list(value, "next_steps")
            current = step.setdefault("next_steps", [])
            if not isinstance(current, list):
                raise StepCliError("last.next_steps must be a list")
            before = list(current)
            merged, _ = dedupe_slugs(current + values)
            step["next_steps"] = merged
            changed = before != merged
    else:
        raise StepCliError(f"unsupported append resource: {args.resource}", EXIT_USAGE)
    if changed:
        write_step_file(path, data, dry_run=args.dry_run)
    emit(result(args, changed))
    return EXIT_OK


def command_patch(args: argparse.Namespace) -> int:
    path = resolve_file(args)
    data = read_step_file(path)
    value = parse_yaml_value(args.value)
    if args.resource == "lessons":
        lessons = ensure_list(value, "lessons")
        data["lessons"], _ = dedupe_normalized(lessons)
    elif args.resource == "last":
        patch = ensure_mapping(value, "last patch")
        step = last_step(data)
        step.update(patch)
    else:
        raise StepCliError(f"unsupported patch resource: {args.resource}", EXIT_USAGE)
    write_step_file(path, data, dry_run=args.dry_run)
    emit(result(args, True))
    return EXIT_OK


def validate_slug(value: Any, label: str) -> None:
    if not isinstance(value, str) or not SLUG_RE.match(value):
        raise StepCliError(f"{label} must be lowercase kebab-case matching {SLUG_RE.pattern}")


def coerce_slug_list(value: Any, name: str) -> list[str]:
    if isinstance(value, str):
        values = [value]
    elif isinstance(value, list):
        values = [str(item) for item in value]
    else:
        raise StepCliError(f"{name} must be a slug string or list of slug strings")
    for slug in values:
        validate_slug(slug.strip(), name)
    return [slug.strip() for slug in values]


def merge_retro(step: dict[str, Any], value: dict[str, Any]) -> bool:
    retro = step.setdefault("retro", {})
    if not isinstance(retro, dict):
        raise StepCliError("last.retro must be a mapping/object")
    changed = False
    for key in ("wins", "issues", "actions"):
        if key not in value:
            continue
        incoming = ensure_list(value[key], f"retro.{key}")
        current = retro.setdefault(key, [])
        if not isinstance(current, list):
            raise StepCliError(f"last.retro.{key} must be a list")
        before = list(current)
        retro[key], _ = dedupe_normalized(current + incoming)
        changed = changed or before != retro[key]
    return changed


def lint_basic(data: dict[str, Any], errors: list[str], warnings: list[str]) -> None:
    if not isinstance(data.get("goal"), str) or not data.get("goal"):
        errors.append("goal must be a non-empty string")
    lessons = data.get("lessons", [])
    if not isinstance(data.get("lessons"), list) or not all(
        isinstance(x, str) for x in lessons
    ):
        errors.append("lessons must be a list of strings")
    steps = data.get("steps")
    if not isinstance(steps, list) or not steps:
        errors.append("steps must be a non-empty list")
        return
    seen: set[str] = set()
    for idx, step in enumerate(steps):
        if not isinstance(step, dict):
            errors.append(f"steps[{idx}] must be a mapping/object")
            continue
        slug = step.get("slug")
        if not isinstance(slug, str) or not SLUG_RE.match(slug):
            errors.append(f"steps[{idx}].slug must be lowercase kebab-case")
        elif slug in seen:
            errors.append(f"steps[{idx}].slug duplicates an earlier step slug: {slug}")
        else:
            seen.add(slug)
    last = steps[-1]
    if isinstance(last, dict):
        if not isinstance(last.get("slug"), str) or not last.get("slug"):
            errors.append("last_step.slug is required")
        if not isinstance(last.get("intent"), str) or not last.get("intent"):
            errors.append("last_step.intent is required")


def lint_step(step: Any, label: str, errors: list[str], warnings: list[str]) -> None:
    if not isinstance(step, dict):
        errors.append(f"{label} must be a mapping/object")
        return
    for key in ("slug", "intent"):
        if not isinstance(step.get(key), str) or not step.get(key):
            errors.append(f"{label}.{key} is required")
    if isinstance(step.get("slug"), str) and not SLUG_RE.match(step["slug"]):
        errors.append(f"{label}.slug must be lowercase kebab-case")
    do = step.get("do")
    if not isinstance(do, dict):
        errors.append(f"{label}.do must be a mapping/object")
    else:
        if not isinstance(do.get("summary"), str) or not do.get("summary"):
            errors.append(f"{label}.do.summary is required")
        if not isinstance(do.get("evidence"), list):
            errors.append(f"{label}.do.evidence must be a list")
    val = step.get("validate")
    if not isinstance(val, dict):
        errors.append(f"{label}.validate must be a mapping/object")
    else:
        if val.get("result") not in {"success", "partial", "failure"}:
            errors.append(f"{label}.validate.result must be success, partial, or failure")
        if not isinstance(val.get("evidence"), list):
            errors.append(f"{label}.validate.evidence must be a list")
    retro = step.get("retro")
    if not isinstance(retro, dict):
        errors.append(f"{label}.retro must be a mapping/object")
    else:
        for key in ("wins", "issues", "actions"):
            if not isinstance(retro.get(key), list):
                errors.append(f"{label}.retro.{key} must be a list")
    next_steps = step.get("next_steps")
    if not isinstance(next_steps, list) or not all(isinstance(x, str) for x in next_steps):
        errors.append(f"{label}.next_steps must be a list of strings")
        next_steps = []
    else:
        for slug in next_steps:
            if not SLUG_RE.match(slug):
                errors.append(f"{label}.next_steps contains invalid slug: {slug}")
    rec = step.get("recommendation")
    if not isinstance(rec, dict):
        errors.append(f"{label}.recommendation must be a mapping/object")
    else:
        if not isinstance(rec.get("next"), str) or not rec.get("next"):
            errors.append(f"{label}.recommendation.next is required")
        if not isinstance(rec.get("rationale"), str) or not rec.get("rationale"):
            errors.append(f"{label}.recommendation.rationale is required")
        if (
            isinstance(rec.get("next"), str)
            and isinstance(next_steps, list)
            and rec.get("next") not in next_steps
        ):
            errors.append(
                f"{label}.recommendation.next is not listed in {label}.next_steps"
            )


def apply_lint_fixes(data: dict[str, Any], level: str, all_steps: bool) -> bool:
    before = yaml.safe_dump(normalize_document(dict_deepcopy(data)), sort_keys=False)
    data.setdefault("lessons", [])
    if isinstance(data.get("lessons"), list):
        data["lessons"], _ = dedupe_normalized(data["lessons"])
    steps = data.get("steps")
    if isinstance(steps, list):
        targets = steps if all_steps else steps[-1:] if steps else []
        for step in targets:
            if not isinstance(step, dict):
                continue
            if isinstance(step.get("next_steps"), list):
                step["next_steps"], _ = dedupe_slugs(step["next_steps"])
            retro = step.get("retro")
            if isinstance(retro, dict):
                for key in ("wins", "issues", "actions"):
                    retro.setdefault(key, [])
                    if isinstance(retro.get(key), list):
                        retro[key], _ = dedupe_normalized(retro[key])
            rec = step.get("recommendation")
            if isinstance(rec, dict) and isinstance(rec.get("next"), str):
                next_steps = step.setdefault("next_steps", [])
                if isinstance(next_steps, list) and rec["next"] not in next_steps:
                    next_steps.append(rec["next"])
                    step["next_steps"], _ = dedupe_slugs(next_steps)
    normalize_document(data)
    after = yaml.safe_dump(data, sort_keys=False)
    return before != after


def dict_deepcopy(value: Any) -> Any:
    return yaml.safe_load(yaml.safe_dump(value, sort_keys=False))


def command_lint(args: argparse.Namespace) -> int:
    path = resolve_file(args)
    data = read_step_file(path)
    if args.fix:
        changed = apply_lint_fixes(data, args.level, args.all)
        if changed:
            write_step_file(path, data, dry_run=args.dry_run)
            if not args.dry_run:
                data = read_step_file(path)
    errors: list[str] = []
    warnings: list[str] = []
    lint_basic(data, errors, warnings)
    if args.level == "complete":
        steps = data.get("steps")
        if isinstance(steps, list) and steps:
            targets = list(enumerate(steps)) if args.all else [(len(steps) - 1, steps[-1])]
            for idx, step in targets:
                lint_step(step, f"steps[{idx}]" if args.all else "last_step", errors, warnings)
    ok = not errors
    emit({
        "ok": ok,
        "level": args.level,
        "errors": errors,
        "warnings": warnings,
        "dry_run": args.dry_run,
    })
    return EXIT_OK if ok else EXIT_LINT


def build_parser() -> argparse.ArgumentParser:
    desc = __doc__ or "STEP YAML helper"
    parser = StepArgumentParser(
        description=desc,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--file", help="STEP-<slug>.yaml path; defaults to STEP_FILE env var")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="preview mutating operations without writing files",
    )
    parser.add_argument("--test", action="store_true", help="run the unittest self-test harness")
    sub = parser.add_subparsers(
        dest="operation",
        required=False,
        parser_class=StepArgumentParser,
    )

    p_init = sub.add_parser("init", help="create a new step file")
    p_init.add_argument("--goal", required=True)
    p_init.add_argument("--slug", required=True)
    p_init.add_argument("--intent", required=True)
    p_init.add_argument("--lesson", action="append", help="initial lesson; may be repeated")
    p_init.add_argument("--force", action="store_true", help="overwrite an existing step file")
    p_init.set_defaults(func=command_init, resource="step")

    p_show = sub.add_parser("show", help="show YAML views")
    p_show.add_argument("resource", choices=["all", "continuation", "goal", "lessons", "last"])
    p_show.set_defaults(func=command_show)

    p_update = sub.add_parser("update", help="update goal or explicit last-step fields")
    p_update.add_argument("resource", choices=["goal", "last"])
    p_update.add_argument("value", nargs="?", help="goal value for 'update goal'")
    p_update.add_argument("--do", dest="do", help="YAML object or '-' for stdin")
    p_update.add_argument("--validate", dest="validate", help="YAML object or '-' for stdin")
    p_update.add_argument("--next-steps", dest="next_steps", help="YAML slug/list or '-' for stdin")
    p_update.add_argument("--recommendation", help="YAML object or '-' for stdin")
    p_update.set_defaults(func=command_update)

    p_append = sub.add_parser("append", help="append lessons, step, or last-step fields")
    p_append.add_argument("resource", choices=["lessons", "step", "last"])
    p_append.add_argument("value", nargs="?", help="lesson value for 'append lessons'")
    p_append.add_argument("--slug")
    p_append.add_argument("--intent")
    p_append.add_argument("--retro", help="YAML object or '-' for stdin")
    p_append.add_argument("--next-steps", dest="next_steps", help="YAML slug/list or '-' for stdin")
    p_append.set_defaults(func=command_append)

    p_patch = sub.add_parser(
        "patch",
        help="ESCAPE HATCH: patch lessons or last; prefer explicit commands",
    )
    p_patch.add_argument("resource", choices=["lessons", "last"])
    p_patch.add_argument("value", help="YAML value or '-' for stdin")
    p_patch.set_defaults(func=command_patch)

    p_lint = sub.add_parser("lint", help="lint step file shape")
    p_lint.add_argument("level", choices=["basic", "complete"])
    p_lint.add_argument(
        "--all",
        action="store_true",
        help="for complete: check every step, not only last",
    )
    p_lint.add_argument("--fix", action="store_true", help="apply safe deterministic fixes only")
    p_lint.set_defaults(func=command_lint, resource="step")
    return parser


def validate_args(args: argparse.Namespace) -> None:
    if args.test:
        return
    if args.operation is None:
        raise StepCliError("operation is required unless --test is supplied", EXIT_USAGE)
    if args.operation == "update" and args.resource == "goal":
        if args.value is None:
            raise StepCliError("update goal requires a value", EXIT_USAGE)
        if any(
            getattr(args, name) is not None
            for name in ("do", "validate", "next_steps", "recommendation")
        ):
            raise StepCliError("update goal does not accept last-step field options", EXIT_USAGE)
    if args.operation == "update" and args.resource == "last" and args.value is not None:
        raise StepCliError("update last does not accept a positional value", EXIT_USAGE)
    if args.operation == "append" and args.resource == "lessons" and args.value is None:
        raise StepCliError("append lessons requires a value", EXIT_USAGE)
    if args.operation == "append" and args.resource in {"step", "last"} and args.value is not None:
        raise StepCliError(f"append {args.resource} does not accept a positional value", EXIT_USAGE)
    if (
        args.operation == "append"
        and args.resource == "step"
        and (not args.slug or not args.intent)
    ):
        raise StepCliError("append step requires --slug and --intent", EXIT_USAGE)


class StepCliSelfTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.step_file = Path(self.tmp.name) / "STEP-self-test.yaml"
        self.script = Path(__file__)

    def run_cli(self, *args: str, expect: int = EXIT_OK) -> subprocess.CompletedProcess[str]:
        cmd = [sys.executable, str(self.script), "--file", str(self.step_file), *args]
        proc = subprocess.run(cmd, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, expect, msg=proc.stderr + proc.stdout)
        return proc

    def test_init_show_and_lint_basic(self) -> None:
        self.run_cli("init", "--goal", "Goal", "--slug", "first-step", "--intent", "Do first")
        shown = yaml.safe_load(self.run_cli("show", "continuation").stdout)
        self.assertEqual(shown["goal"], "Goal")
        self.assertEqual(shown["last_step"]["slug"], "first-step")
        linted = yaml.safe_load(self.run_cli("lint", "basic").stdout)
        self.assertTrue(linted["ok"])

    def test_update_append_and_complete_lint(self) -> None:
        self.run_cli("init", "--goal", "Goal", "--slug", "first-step", "--intent", "Do first")
        self.run_cli("update", "last", "--do", '{summary: "Did", evidence: ["file"]}')
        self.run_cli("update", "last", "--validate", '{result: success, evidence: ["checked"]}')
        self.run_cli("append", "last", "--retro", '{wins: ["won"], issues: [], actions: []}')
        self.run_cli("append", "last", "--next-steps", "second-step")
        self.run_cli("update", "last", "--recommendation", '{next: second-step, rationale: "Next"}')
        linted = yaml.safe_load(self.run_cli("lint", "complete").stdout)
        self.assertTrue(linted["ok"])

    def test_lint_fix_back_propagates_recommendation(self) -> None:
        self.run_cli("init", "--goal", "Goal", "--slug", "first-step", "--intent", "Do first")
        self.run_cli("update", "last", "--recommendation", '{next: second-step, rationale: "Next"}')
        self.run_cli("lint", "complete", "--fix", expect=EXIT_LINT)
        shown = yaml.safe_load(self.run_cli("show", "last").stdout)
        self.assertIn("second-step", shown["last_step"]["next_steps"])

    def test_dry_run_does_not_write(self) -> None:
        self.run_cli("init", "--goal", "Goal", "--slug", "first-step", "--intent", "Do first")
        cmd = [
            sys.executable,
            str(self.script),
            "--file",
            str(self.step_file),
            "--dry-run",
            "append",
            "lessons",
            "Dry run lesson",
        ]
        proc = subprocess.run(cmd, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, EXIT_OK, msg=proc.stderr + proc.stdout)
        self.assertTrue(yaml.safe_load(proc.stdout)["dry_run"])
        shown = yaml.safe_load(self.run_cli("show", "lessons").stdout)
        self.assertNotIn("Dry run lesson", shown["lessons"])


def run_self_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(StepCliSelfTest)
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)
    emit({"ok": result.wasSuccessful(), "tests": result.testsRun})
    return EXIT_OK if result.wasSuccessful() else EXIT_USAGE


def main() -> int:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    parser = build_parser()
    try:
        args = parser.parse_args()
        if yaml is None:
            log.error("PyYAML is required; install it with `pip install PyYAML`")
            return EXIT_SCHEMA
        validate_args(args)
        if args.test:
            return run_self_tests()
        return args.func(args)
    except StepCliError as exc:
        log.error(str(exc))
        return exc.code
    except BrokenPipeError:
        return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
