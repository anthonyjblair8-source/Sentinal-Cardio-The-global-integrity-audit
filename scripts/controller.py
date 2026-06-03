import subprocess
import os

# COPILOT HOOK: Add new audit targets to this list via Copilot
AUDIT_MANIFEST = [
    ".github/scripts/audit_doj.sh",
    "data/doj_records/",
]

def run_orchestration():
    for target in AUDIT_MANIFEST:
        if os.path.isfile(target):
            print(f"Running audit script: {target}")
            subprocess.run(["bash", target], check=True)
        elif os.path.isdir(target):
            print(f"Scanning data directory: {target}")
            for root, dirs, files in os.walk(target):
                for file in files:
                    print(f"Found file: {os.path.join(root, file)}")
        else:
            print(f"ERROR: Target {target} not found.")

if __name__ == "__main__":
    run_orchestration()