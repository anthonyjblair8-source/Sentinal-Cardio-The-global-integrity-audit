import spacy
from collections import defaultdict
import os
import json

# Load NLP library
nlp = spacy.load("en_core_web_sm")

# Files & keywords setup
log_file = "repository_integrity_log.txt"
report_file = "nlp_analysis_report.json"

def analyze_log(filepath):
    """Perform NLP analysis on the audit log."""
    entity_map = defaultdict(list)

    if not os.path.exists(filepath):
        print(f"ERROR: Log file {filepath} does not exist!")
        return entity_map

    with open(filepath, 'r') as file:
        for line in file:
            doc = nlp(line)
            for ent in doc.ents:
                entity_map[ent.label_].append(ent.text)

    return entity_map

def generate_report(entity_map, output_file):
    """Generate JSON report with keyword insights."""
    with open(output_file, 'w') as f:
        json.dump(entity_map, f, indent=4)
    print(f"NLP report generated: {output_file}")

if __name__ == "__main__":
    print("===== NLP Audit Analysis =====")
    print("Analyzing log file. Please wait...\n")
    entity_insights = analyze_log(log_file)

    if entity_insights:
        print(f"Entities detected: {json.dumps(entity_insights, indent=2)}")
        generate_report(entity_insights, report_file)
    else:
        print("No entities detected or log file is empty.")