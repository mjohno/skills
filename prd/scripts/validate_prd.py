#!/usr/bin/env python3
import re
import json
import sys
import argparse

# --- Configuration ---
VAGUE_WORDS = ["fast", "easy", "robust", "efficient", "seamless", "optimized", "quickly", "smooth", "user-friendly"]
MANDATORY_SECTIONS = [
    "Executive Summary",
    "Strategic Goals",
    "User Stories",
    "Acceptance Criteria"
]

# Regex Patterns
# User Story: As a [role], I want [action], so that [value]
USER_STORY_PATTERN = r"As a .+, I want .+, so that .+"

# Gherkin: Given/When/Then
GHERKIN_KEYWORDS = ["Given", "When", "Then"]

class PRDValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""
        self.report = {
            "file": file_path,
            "passed": True,
            "heuristics": [],
            "semantic_pending": False,
            "semantic_prompts": []
        }

    def load(self):
        try:
            with open(self.file_path, 'r') as f:
                self.content = f.read()
        except Exception as e:
            self.report["passed"] = False
            self.report["heuristics"].append({"type": "ERROR", "message": f"Failed to read file: {str(e)}"})
            return False
        return True

    def check_sections(self):
        for section in MANDATORY_SECTIONS:
            if section not in self.content:
                self.report["passed"] = False
                self.report["heuristics"].append({
                    "type": "MISSING_SECTION",
                    "message": f"Mandatory section '{section}' is missing."
                })

    def check_vague_words(self):
        found_vague = []
        for word in VAGUE_WORDS:
            # Use word boundaries to avoid partial matches
            if re.search(rf"\b{word}\b", self.content, re.IGNORECASE):
                found_vague.append(word)
        
        if found_vague:
            self.report["heuristics"].append({
                "type": "VAGUE_LANGUAGE",
                "message": f"Potential vague words detected: {', '.join(found_vague)}",
                "words": found_vague
            })

    def check_syntax(self):
        # Check User Stories
        # We look for lines that look like User Stories but fail the pattern
        lines = self.content.split('\n')
        for line in lines:
            if "As a" in line and "I want" in line and "so that" in line:
                if not re.match(USER_STORY_PATTERN, line, re.IGNORECASE):
                    self.report["passed"] = False
                    self.report["heuristics"].append({
                        "type": "SYNTAX_ERROR",
                        "message": f"User Story does not follow standard pattern: '{line.strip()}'"
                    })
            elif "As a" in line or "I want" in line or "so that" in line:
                # This is a heuristic for "it looks like it's trying to be a story but failed"
                self.report["semantic_pending"] = True
                self.report["semantic_prompts"].append(f"Verify if this line is a valid User Story: '{line.strip()}'")

        # Check Gherkin
        gherkin_found = False
        for keyword in GHERKIN_KEYWORDS:
            if re.search(rf"\b{keyword}\b", self.content):
                gherkin_found = True
                break
        
        if not gherkin_found:
            self.report["passed"] = False
            self.report["heuristics"].append({
                "type": "MISSING_GHERKIN",
                "message": "No Gherkin syntax (Given/When/Then) found in Acceptance Criteria."
            })
        else:
            # If Gherkin is found, we flag semantic pending to ensure the LLM checks the logic
            self.report["semantic_pending"] = True
            self.report["semantic_prompts"].append("Perform a semantic audit of the Gherkin scenarios for logical completeness and edge cases.")

    def validate(self):
        if not self.load():
            return self.report

        self.check_sections()
        self.check_vague_words()
        self.check_syntax()

        # If we have heuristic errors, it's not "passed"
        if any(h["type"] in ["MISSING_SECTION", "SYNTAX_ERROR", "MISSING_GHERKIN"] for h in self.report["heuristics"]):
            self.report["passed"] = False

        return self.report

def main():
    parser = argparse.ArgumentParser(description="Validate PRD compliance.")
    parser.add_argument("file", help="Path to the PRD file")
    args = parser.parse_args()

    validator = PRDValidator(args.file)
    report = validator.validate()

    print(json.dumps(report, indent=2))
    
    # Exit codes for agentic integration
    if not report["passed"]:
        sys.exit(1)
    if report["semantic_pending"]:
        # Exit with 0 but the JSON tells the agent there's more to do
        sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    main()
