import subprocess
import re
import time

# Keywords to track for the hashtag matrix
KEYWORDS = ["Epstein", "JFK", "9/11", "pizzagate", "REDACTED", "CLASSIFIED", "OMITTED"]

# Initialize the hashtag matrix
hashtag_matrix = {keyword: 0 for keyword in KEYWORDS}

def run_audit():
    """
    Runs the audit script and captures real-time output.
    """
    process = subprocess.Popen(
        ["bash", ".github/scripts/audit_doj.sh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("===== REAL-TIME AUDIT CONSOLE =====")
    print("Running audit... Capturing logs!\n")

    try:
        # Read the output line by line
        for line in iter(process.stdout.readline, ''):
            print(line.strip())  # Print real-time output

            # Check for keywords and update the hashtag matrix
            for keyword in KEYWORDS:
                if re.search(rf"\b{keyword}\b", line, re.IGNORECASE):
                    hashtag_matrix[keyword] += 1

            # Visualize the hashtag matrix every second
            print("\n===== HASHTAG MATRIX =====")
            for hashtag, count in hashtag_matrix.items():
                print(f"{hashtag}: {'#' * count}")
            print("\n")

            # Slight delay for output visualization
            time.sleep(1)

    except KeyboardInterrupt:
        print("Audit interrupted!")
    finally:
        # Ensure the process is terminated
        process.terminate()
        process.wait()

if __name__ == "__main__":
    run_audit()