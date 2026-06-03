import hashlib
import os
import json

# Configurations
file_paths = [
    ".github/scripts/audit_doj.sh",
    "data/doj_records/",
    "scripts/controller.py",
]
checksum_file = "checksums.json"


def generate_checksums(file_paths):
    """Generate SHA-256 checksums for given files."""
    checksums = {}
    for path in file_paths:
        try:
            if os.path.isfile(path):
                with open(path, "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                checksums[path] = file_hash
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        with open(full_path, "rb") as f:
                            file_hash = hashlib.sha256(f.read()).hexdigest()
                        checksums[full_path] = file_hash
        except Exception as e:
            print(f"Error processing {path}: {e}")

    return checksums


def verify_checksums(checksums, file_paths):
    """Verify files against stored checksums."""
    discrepancies = {}
    for path in file_paths:
        try:
            if path in checksums:
                with open(path, "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                if checksums[path] != file_hash:
                    discrepancies[path] = "Hash mismatch! File may be altered."
            else:
                discrepancies[path] = "File not found in checksums."
        except FileNotFoundError:
            discrepancies[path] = "File not found."

    return discrepancies


def load_checksums(checksum_file):
    """Load checksums from a file."""
    if not os.path.exists(checksum_file):
        return {}
    with open(checksum_file, 'r') as f:
        return json.load(f)


def save_checksums(checksums, checksum_file):
    """Save checksums to a file."""
    with open(checksum_file, 'w') as f:
        json.dump(checksums, f, indent=4)


if __name__ == "__main__":
    print("===== Checksum Validator =====")
    print("1. Generate and save checksums")
    print("2. Verify file integrity")
    choice = input("Select an option: ")

    if choice == "1":
        checksums = generate_checksums(file_paths)
        save_checksums(checksums, checksum_file)
        print(f"Checksums saved to {checksum_file}")

    elif choice == "2":
        existing_checksums = load_checksums(checksum_file)
        discrepancies = verify_checksums(existing_checksums, file_paths)
        for path, message in discrepancies.items():
            print(f"{path}: {message}")

    else:
        print("Invalid choice. Exiting.")