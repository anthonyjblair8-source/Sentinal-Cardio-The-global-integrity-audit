# Sentinel Cardio – Global Integrity Audit (Single‑File Build v0.1.0)
# Author: anthonyjblair8-source

import hashlib
from pathlib import Path
from collections import Counter
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Sentinel Cardio – Global Integrity Audit")


# ---------------------------------------------------------
# 1. SHA‑256 INTEGRITY ENGINE
# ---------------------------------------------------------

def compute_sha256(path: str) -> str:
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def verify_checksum(path: str, expected_hash: str) -> dict:
    actual = compute_sha256(path)
    passed = actual.lower() == expected_hash.lower()

    return {
        "path": path,
        "expected_hash": expected_hash,
        "actual_hash": actual,
        "passed": passed,
        "status": "PASS" if passed else "FAIL"
    }


# ---------------------------------------------------------
# 2. LOG ANOMALY DETECTOR
# ---------------------------------------------------------

def load_log_lines(path: str) -> list[str]:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Log file not found: {path}")
    return [line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def detect_frequency_anomalies(path: str, z_threshold: float = 2.5) -> dict:
    lines = load_log_lines(path)
    counts = Counter(lines)

    values = np.array(list(counts.values()), dtype=float)
    if len(values) == 0:
        return {"anomalies": [], "summary": "no data"}

    mean = values.mean()
    std = values.std() if values.std() > 0 else 1.0

    anomalies = []
    for line, count in counts.items():
        z = (count - mean) / std
        if abs(z) >= z_threshold:
            anomalies.append({
                "line": line,
                "count": count,
                "z_score": float(z)
            })

    return {
        "anomalies": anomalies,
        "mean": float(mean),
        "std": float(std),
        "total_unique_lines": len(counts)
    }


# ---------------------------------------------------------
# 3. API MODELS
# ---------------------------------------------------------

class IntegrityRequest(BaseModel):
    path: str
    expected_hash: str


class LogAnomalyRequest(BaseModel):
    path: str
    z_threshold: float = 2.5


# ---------------------------------------------------------
# 4. API ROUTES
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "service": "Sentinel Cardio",
        "status": "operational",
        "version": "0.1.0"
    }


@app.post("/integrity/check")
def integrity_check(req: IntegrityRequest):
    return verify_checksum(req.path, req.expected_hash)


@app.post("/logs/anomalies")
def log_anomalies(req: LogAnomalyRequest):
    return detect_frequency_anomalies(req.path, req.z_threshold)
