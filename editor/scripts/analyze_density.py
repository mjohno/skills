import sys
import re
import json
import argparse

# Predefined lists for heuristic analysis
FUNCTION_WORDS = {
    'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'so', 'yet', 'at', 'by', 'from', 'in', 'into', 'of', 'off', 'on', 'onto', 'out', 'over', 'to', 'up', 'with', 'as', 'if', 'about', 'above', 'after', 'against', 'along', 'among', 'around', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'during', 'except', 'for', 'from', 'in', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'over', 'past', 'since', 'through', 'throughout', 'till', 'to', 'toward', 'under', 'until', 'up', 'upon', 'with', 'within', 'without',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs',
    'is', 'am', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did'
}

WORDY_PHRASES = [
    r"in order to",
    r"due to the fact that",
    r"it is important to note that",
    r"at this point in time",
    r"in the event that",
    r"with regard to",
    r"a large number of",
    r"in spite of the fact that",
    r"as a matter of fact",
    r"it should be noted that",
    r"on a daily basis",
    r"for the purpose of",
]

REDUNDANT_PAIRS = [
    r"added bonus",
    r"end result",
    r"past history",
    r"summarize briefly",
    r"completely finished",
    r"advance warning",
    r"close proximity",
    r"actual facts",
    r"basic fundamentals",
    r"consensus of opinion",
]

PASSIVE_VOICE_PATTERN = re.compile(r"\b(is|are|was|were|been|being)\s+\w+ed\b", re.IGNORECASE)

def analyze_text(text):
    # Clean text: remove punctuation and normalize whitespace
    clean_text = re.sub(r'[^\w\s]', '', text)
    words = clean_text.split()
    
    if not words:
        return {
            "summary": {"density_score": 0, "wordiness_score": 0, "passive_voice_count": 0, "redundancy_count": 0},
            "details": {"wordy_phrases": [], "passive_indices": [], "redundant_phrases": []}
        }

    # 1. Density Calculation
    content_count = 0
    function_count = 0
    for word in words:
        if word.lower() in FUNCTION_WORDS:
            function_count += 1
        else:
            content_count += 1
    
    # Avoid division by zero
    density_score = content_count / function_count if function_count > 0 else float(content_count)

    # 2. Wordiness Detection
    wordy_found = []
    for phrase in WORDY_PHRASES:
        matches = re.finditer(phrase, text, re.IGNORECASE)
        for match in matches:
            wordy_found.append({
                "phrase": match.group(),
                "start": match.start(),
                "end": match.end()
            })
    
    wordiness_score = len(wordy_found) / len(words) if words else 0

    # 3. Passive Voice Detection
    passive_indices = []
    for match in PASSIVE_VOICE_PATTERN.finditer(text):
        passive_indices.append({
            "phrase": match.group(),
            "start": match.start(),
            "end": match.end()
        })

    # 4. Redundancy Detection
    redundant_found = []
    for pair in REDUNDANT_PAIRS:
        matches = re.finditer(pair, text, re.IGNORECASE)
        for match in matches:
            redundant_found.append({
                "phrase": match.group(),
                "start": match.start(),
                "end": match.end()
            })

    return {
        "summary": {
            "density_score": round(density_score, 2),
            "wordiness_score": round(wordiness_score, 4),
            "passive_voice_count": len(passive_indices),
            "redundancy_count": len(redundant_found)
        },
        "details": {
            "wordy_phrases": [f"{m['phrase']} (at {m['start']})" for m in wordy_found],
            "passive_indices": [f"{m['phrase']} (at {m['start']})" for m in passive_indices],
            "redundant_phrases": [f"{m['phrase']} (at {m['start']})" for m in redundant_found]
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze text for conciseness and density.")
    parser.add_argument("file", help="Path to the text file to analyze.")
    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        results = analyze_text(text)
        print(json.dumps(results, indent=2))

    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
