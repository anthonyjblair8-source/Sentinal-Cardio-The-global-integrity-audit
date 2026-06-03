# Contributing to Sentinel Cardio

## Thank you for contributing!
We're excited to have you get involved. By contributing to this repository, you help us enhance the integrity and functionality of Sentinel Cardio.

---

## Ways to Contribute
1. **Report Issues**:
   - File bug reports using the `Bug Report` template.
   - Suggest enhancements using the `Feature Request` template.

2. **Submit Pull Requests**:
   - Use the `Pull Request Template` for submissions.
   - Ensure that your code passes all relevant tests and aligns with the coding standards used in this repository.

3. **Run Automated Workflow Tests**:
   - Before submission, test your changes locally and ensure workflows pass in GitHub Actions.

4. **Enhance Documentation**:
   - Improve the `README`, comments in scripts, and documentation.

---

## Development Setup
### 1. Clone the Repository
```bash
git clone https://github.com/anthonyjblair8-source/Sentinal-Cardio-The-global-integrity-audit.git
cd Sentinal-Cardio-The-global-integrity-audit
```

### 2. Python Environment
Ensure you are using **Python 3.11** (or above):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Test the System
Run the test scripts:
```bash
python scripts/audit_terminal.py
python scripts/nlp_audit_analysis.py
```

For the Streamlit dashboard:
```bash
streamlit run scripts/audit_dashboard.py
```

---

## Code Guidelines
1. **Code Style**:
   - Follow [PEP8](https://peps.python.org/pep-0008/) guidelines.
   - Use meaningful variable and function names.

2. **Write Comments**:
   - Add comments to explain your logic, especially for complex sections.

3. **Testing**:
   - Ensure your changes are covered by existing or new tests.

---

Thank you for your contribution!