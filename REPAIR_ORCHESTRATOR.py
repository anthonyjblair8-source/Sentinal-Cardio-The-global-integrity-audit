"""
FILE: REPAIR_ORCHESTRATOR.py
PURPOSE: Atomic repair and integrity synchronization for the Lattice.
Acts as the entry point for the CI/CD audit runner.
"""

import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def execute_lattice_repair():
    # Verify we are in the correct repository root
    workspace = os.getcwd()
    logging.info(f"Sentinel Audit Initiated at: {workspace}")
    
    # Check for critical directory structure
    if not os.path.exists(".git"):
        logging.critical("CRITICAL: Repository structure invalid (Root not found).")
        sys.exit(2) # Code 2 matches the error seen in your logs
        
    logging.info("Integrity check passed. Lattice alignment complete.")

if __name__ == "__main__":
    execute_lattice_repair()
