import os
import time

# Configuration
log_file = "repository_integrity_log.txt"
optimized_log_file = "optimized_audit_log.txt"


def optimize_audit_log(input_file, output_file):
    """
    Optimizes the structure of an audit log for faster parsing and reduced redundancy.
    """
    if not os.path.exists(input_file):
        print(f"Input log file {input_file} does not exist.")
        return False

    # Example optimization: Remove duplicate lines, sort entries
    seen_lines = set()
    optimized_lines = []

    with open(input_file, 'r') as infile:
        for line in infile:
            if line not in seen_lines:
                seen_lines.add(line)
                optimized_lines.append(line)

    with open(output_file, 'w') as outfile:
        outfile.writelines(sorted(optimized_lines))

    print(f"Optimized log saved to {output_file}")
    return True


def monitor_performance(func):
    """
    Measures the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result

    return wrapper

# Apply performance monitor to optimize_audit_log
optimized_function = monitor_performance(optimize_audit_log)

if __name__ == "__main__":
    print("===== Audit Log Performance Optimization =====")
    optimized_function(log_file, optimized_log_file)