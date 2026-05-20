import hashlib
import time

def calculate_3mi():
    data_input = "Persistence_Governance_Alpha"
    encoded = data_input.encode('utf-8')
    hash_val = hashlib.sha256(encoded).hexdigest()
    return int(hash_val[:8], 16) / 4294967295

def mint_token():
    unique_string = str(time.time())
    token = hashlib.sha256(unique_string.encode()).hexdigest()
    return f"SC-TOKEN-{token[:12].upper()}"

if __name__ == "__main__":
    print("--- SENTINEL ENGINE INITIATED ---")
    print(f"3MI Index: {calculate_3mi():.6f}")
    print(f"Persistence Token: {mint_token()}")
    print("--- SYSTEM STATUS: OPERATIONAL ---")