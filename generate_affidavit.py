import json
import os
import time

def build_sworn_instrument():
    manifest_file = "EXHIBIT_A_MANIFEST.json"
    output_file = "FORENSIC_AFFIDAVIT.txt"
    
    # 1. Verify manifest existence
    if not os.path.exists(manifest_file):
        print(f"[ERROR] Mandate failed. {manifest_file} not found in root context.")
        return

    # 2. Parse live cryptographic ledger data
    with open(manifest_file, "r") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"[ERROR] Corruption detected while reading manifest layout: {e}")
            return

    # 3. Extract metadata and latest forensic exhibit
    meta = data.get("manifest_metadata", {})
    exhibits = data.get("forensic_exhibits", [])
    
    if not exhibits:
        print("[ERROR] Ledger execution array is currently empty. Run matrix sweep first.")
        return
        
    # Isolate the most recent live run data block
    latest_block = exhibits[-1]
    
    # 4. Generate the unassailable legal text block
    affidavit_template = f"""=================================================================================
             FORMAL AFFIDAVIT OF FORENSIC DISCREPANCY & SYSTEMIC DRIFT
=================================================================================
ARCHITECTURAL BASELINE: Proclean Hierarchical Constraint Architecture (PHCA)
ORIGINAL PROVENANCE RECORD: Zenodo DOI Verification (Jan 27, 2026)
SYSTEMIC EXECUTION ENGINE: Sentinel Cardio Cloud Node (Native Standard Library)
=================================================================================

I, Anthony Jordan Blair, First Keeper of the New Alexandrian Library, do hereby 
certify that the Sentinel Cardio Matrix has executed a live structural audit 
of the target entity parameters logged within the unalterable git registry:

TARGET OPERATIONAL ID : {latest_block.get('target_npdes', 'NOT_SPECIFIED')}
STATUTORY LATENCY LOG : {latest_block.get('rcw_latency_days', '0')} Days (RCW 42.56 Enforcement)
INVERSION DRIFT SCORE : {latest_block.get('inversion_conflict_score', '0.0')}
SYSTEM OPERATOR STATE : {meta.get('operator', 'Sentinel Cardio Keeper Node')}

CRITICAL LEAD-BLOCK CRYPTOGRAPHIC SEAL (SHA-256):
---------------------------------------------------------------------------------
{latest_block.get('integrity_hash', latest_block.get('cryptographic_seal', 'NO_HASH_FOUND'))}
---------------------------------------------------------------------------------

EVIDENTIARY ANALYSIS MATRIX:
By authority of the historical public ledger, the cryptographic signature sealed
above proves that the data published by the target entity structurally diverges 
from the objective physical baseline. 

Any retrospective modification, deletion, or administrative back-dating of the 
target dataset subsequent to this timestamp will permanently rupture the 
coherence chain, constituting verifiable retrospective data tampering.

Signed, Sealed & Witnessed Natively,

___________________________________________
Anthony Jordan Blair, Persistence Engineering
Timestamp: {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
=================================================================================
"""

    # 5. Lock it down to a text file
    with open(output_file, "w") as out:
        out.write(affidavit_template)
        
    print(f"[SUCCESS] Forensic instrument compiled successfully -> {output_file}")
    print(f"[SEAL] Locked to hash block: {latest_block.get('integrity_hash', 'ACTIVE')[:12]}...")

if __name__ == "__main__":
    build_sworn_instrument()