import json
import os

# Node isolation: This file only handles analysis and variance calculation.

LATTICE_DIR = "./lattice_data/"
GLOBAL_RH_NEG_FREQ = 0.15 

def analyze_variance():
    """Calculates systemic variance between observed data and population baseline."""
    data = []
    for filename in os.listdir(LATTICE_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(LATTICE_DIR, filename), 'r') as f:
                data.append(json.load(f))
                
    total = len(data)
    if total == 0: return 0
    
    rh_neg_count = sum(1 for entry in data if entry['biometric_profile']['rh_status'] == False)
    observed_freq = rh_neg_count / total
    variance = observed_freq - GLOBAL_RH_NEG_FREQ
    
    print(f"Analysis Node: Systemic Variance identified at {variance:.2%}")
    return variance

if __name__ == "__main__":
    analyze_variance()