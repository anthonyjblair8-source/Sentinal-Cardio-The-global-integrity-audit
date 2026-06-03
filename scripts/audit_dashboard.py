import streamlit as st
import time
import os
from collections import defaultdict

def read_audit_log(filepath):
    """Read the audit log and count keyword occurrences."""
    keywords = ["Epstein", "JFK", "9/11", "pizzagate", "REDACTED", "CLASSIFIED", "OMITTED"]
    hashtag_matrix = defaultdict(int)

    # Check if file exists
    if not os.path.exists(filepath):
        return hashtag_matrix

    with open(filepath, 'r') as f:
        for line in f:
            for keyword in keywords:
                if keyword.lower() in line.lower():
                    hashtag_matrix[keyword] += 1
    
    return hashtag_matrix

# Streamlit Web UI
st.title("Sentinel Cardio: Real-Time Audit Dashboard")
st.write("Visualizing audit findings and hashtag metrics in real-time.")

log_file = "repository_integrity_log.txt"

if not os.path.exists(log_file):
    st.error(f"Log file not found: {log_file}. Please ensure audits are running.")
else:
    st.sidebar.title("Dashboard Options")
    refresh_rate = st.sidebar.slider("Refresh Rate (seconds):", min_value=1, max_value=60, value=5)

    st.write("### Audit Findings")
    st.text_area("Audit Log Output:", value=open(log_file).read(), height=300, key="log_output")

    st.write("### Hashtag Occurrence Matrix")
    while True:
        hashtag_matrix = read_audit_log(log_file)
        for hashtag, count in hashtag_matrix.items():
            st.metric(label=hashtag, value=count)
        time.sleep(refresh_rate)
