# MKF Bundle Discovery

## Contract

MKF knowledge lives in one or more filesystem bundle roots.

## Environment Variables

- `MKF_BUNDLES` is a semicolon-delimited list of bundle tokens.
- Split on `;`.
- Trim whitespace.
- Ignore empty entries, including trailing semicolon entries.
- Normalize tokens to uppercase.
- Treat `-` and `_` as equivalent by converting `-` to `_` for environment variable lookup.
- Resolve each normalized token through `MKF_<NAME>_BUNDLE`.
- If `MKF_BUNDLES` is unset or empty after splitting/trimming, no environment-configured bundles are available.

Example:

```sh
MKF_BUNDLES=GENERAL;PHOENIX;MY-BUNDLE;
MKF_GENERAL_BUNDLE=/knowledge/general
MKF_PHOENIX_BUNDLE=/knowledge/phoenix
MKF_MY_BUNDLE_BUNDLE=/knowledge/my-bundle
```

## Prompt Selectors

Operational skills may accept:

- configured bundle names, e.g. `general`, `GENERAL`, `my-bundle`, `my_bundle`
- explicit filesystem paths to use directly as bundle roots
- multiple bundle selectors for lookup
- exactly one unambiguous bundle selector for record

## Resolution Order

1. Use explicit prompt-provided filesystem paths directly when present and valid.
2. Match prompt selectors against normalized configured bundle names.
3. Use all configured bundles only when the operation explicitly supports or requests all-bundle behavior.
4. Ask for clarification when record target selection is missing or ambiguous.

## Bundle Record

A resolved bundle should carry:

```yaml
name: GENERAL
root: /knowledge/general
source: env | prompt-path
```

## Errors

Report unresolved selectors, missing `MKF_<NAME>_BUNDLE` variables, and non-existent bundle paths clearly.
