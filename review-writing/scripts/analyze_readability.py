import sys
import re
import json
import math
import statistics

def tokenize_sentences(text):
    """
    Splits text into sentences using a regex-based approach.
    Note: This is a simplified tokenizer and may struggle with abbreviations.
    """
    # Regex to split on . ! ? followed by whitespace or end of string
    sentence_endings = re.compile(r'(?<=[.!?])\s+')
    sentences = sentence_endings.split(text.strip())
    # Filter out empty strings
    return [s for s in sentences if s.strip()]

def tokenize_words(sentence):
    """Splits a sentence into words, ignoring punctuation."""
    return re.findall(r'\w+', sentence)

def calculate_log_normal_params(mu_x, sigma_x):
    """
    Converts arithmetic mean and std dev to log-normal parameters (mu_log, sigma_log).
    """
    sigma_log_sq = math.log(1 + (sigma_x**2 / mu_x**2))
    sigma_log = math.sqrt(sigma_log_sq)
    mu_log = math.log(mu_x) - 0.5 * sigma_log_sq
    return mu_log, sigma_log

def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        return {"error": f"Could not read file: {str(e)}"}

    sentences = tokenize_sentences(text)
    if not sentences:
        return {"error": "No sentences found in the provided text."}

    sentence_lengths = [len(tokenize_words(s)) for s in sentences]
    
    # Target parameters
    TARGET_MU_X = 15
    TARGET_SIGMA_X = 5
    UPPER_BOUND = 30
    SHORT_THRESHOLD = 4 # Fixed threshold for "too short"
    
    # Statistical Summary
    summary = {
        "total_sentences": len(sentences),
        "total_words": sum(sentence_lengths),
        "mean_length": statistics.mean(sentence_lengths),
        "median_length": statistics.median(sentence_lengths),
        "variance": statistics.variance(sentence_lengths) if len(sentence_lengths) > 1 else 0,
        "std_dev": statistics.stdev(sentence_lengths) if len(sentence_lengths) > 1 else 0,
        "min_length": min(sentence_lengths),
        "max_length": max(sentence_lengths)
    }

    # Identify Outliers
    too_short = []
    too_long = []

    for idx, length in enumerate(sentence_lengths):
        if length <= SHORT_THRESHOLD:
            too_short.append({
                "index": idx,
                "length": length,
                "text": sentences[idx].strip()
            })
        elif length > UPPER_BOUND:
            too_long.append({
                "index": idx,
                "length": length,
                "text": sentences[idx].strip()
            })

    # Cluster Detection (Sliding Window)
    # Detect segments where the local average sentence length exceeds target mu.
    clusters = []
    window_size = 5
    for i in range(len(sentence_lengths) - window_size + 1):
        window = sentence_lengths[i : i + window_size]
        local_avg = statistics.mean(window)
        if local_avg > TARGET_MU_X:
            # Check if this is part of an existing cluster to avoid overlap
            if not clusters or clusters[-1]["end"] < i:
                clusters.append({"start": i, "end": i + window_size - 1, "avg_length": local_avg})
            else:
                clusters[-1]["end"] = i + window_size - 1
                clusters[-1]["avg_length"] = local_avg # Keep the most recent/extreme

    report = {
        "summary": summary,
        "outliers": {
            "too_short": too_short,
            "too_long": too_long
        },
        "high_density_clusters": clusters
    }

    return report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python analyze_length.py <file_path>"}))
        sys.exit(1)

    file_to_analyze = sys.argv[1]
    result = analyze_text(file_to_analyze)
    print(json.dumps(result, indent=2))
