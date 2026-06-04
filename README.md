# Sentinel Cardio: The Global Integrity Audit

Sentinel Cardio is an advanced auditing and monitoring system designed to analyze sensitive data, detect anomalies, ensure data integrity, and optimize performance. This robust framework helps organizations maintain transparency and security throughout their workflows.

---

## Key Features

### **1. Real-Time Monitoring**
- **Dashboard**: The `audit_dashboard.py` provides real-time visualization of audit logs and dynamic hashtag matrices for keyword tracking.
- Easily monitor ongoing audits and keyword occurrences.

### **2. Natural Language Processing (NLP)**
- `nlp_audit_analysis.py` extracts contextual entities, including names, locations, and organizations, from audit logs.
- Generates a JSON report categorizing key data insights.

### **3. Modular Integrity and Performance Checks**
- **Checksum Validation** (`checksum_validator.py`): Verifies file integrity using SHA-256 checksums.
- **Pattern Anomaly Detection** (`anomaly_detector.py`): Identifies unexpected patterns in logs using advanced machine learning algorithms.
- **Performance Optimization** (`performance_optimizer.py`): Optimizes audit logs, removes redundancy, and tracks execution time for enhanced efficiency.

### **4. Collaborative Contribution**
- Pre-configured templates for bug reports, feature requests, and pull requests.
- Clear contributor guidelines ensure seamless onboarding for new contributors.

---

## How It Works

1. **Run Audits**:
   - Execute `audit_doj.sh` to scan directories for sensitive keywords like "REDACTED" and "CLASSIFIED".

2. **Visualize Data**:
   - Use `audit_dashboard.py` for real-time keyword tracking.

3. **Analyze Logs**:
   - NLP processing (`nlp_audit_analysis.py`) provides context insights.
   - Anomaly detection (`anomaly_detector.py`) alerts you to suspicious activity.
   - Performance optimization (`performance_optimizer.py`) streamlines audit logs for faster analysis.

4. **Verify Integrity**:
   - Run `checksum_validator.py` to ensure files remain unaltered.

---

## Quick Start
```bash
# Clone the repository
git clone https://github.com/anthonyjblair8-source/Sentinal-Cardio-The-global-integrity-audit.git
cd Sentinal-Cardio-The-global-integrity-audit

# Install dependencies
pip install -r requirements.txt

# Run audits
bash .github/scripts/audit_doj.sh

# Start the dashboard
streamlit run scripts/audit_dashboard.py
```

---

## Contributing
We welcome community contributions! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
[MIT License](LICENSE)
