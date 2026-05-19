import argparse

def run_demo():
    print("Running Sentinel Cardio Demo...")
    # Add demo-specific logic here

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sentinel Cardio CLI")
    parser.add_argument("--run-demo", action="store_true", help="Run the Sentinel Cardio demo")

    args = parser.parse_args()

    if args.run_demo:
        run_demo()