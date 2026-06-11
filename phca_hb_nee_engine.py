"""
PHCA–H/B–NEE symbolic engine core for Sentinel-Cardio.

This module is self-contained and safe to import from other files, e.g.:

    from phca_hb_nee_engine import (
        NodeState, update_node, default_governance_state, default_alpha
    )
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List
import math
import time


# ---------- Core data structures ----------

@dataclass
class PHCAState:
    P: Any   # structural representation
    H: Any   # contextual representation
    C: Any   # semantic/domain representation
    A: Any   # pattern/rhythm representation


@dataclass
class HermeticState:
    HCP: float          # correspondence score
    HPP: Dict[str, int] # polarity map
    HRP: Dict[str, Any] # rhythm/cycle descriptor


@dataclass
class BayesianState:
    priors: Dict[Any, float]
    posteriors: Dict[Any, float]


@dataclass
class EnergyState:
    value: float
    components: Dict[str, float]


@dataclass
class MnemosyneLogEntry:
    phca: PHCAState
    hermetic: HermeticState
    bayes: BayesianState
    energy: EnergyState
    event: str
    metadata: Dict[str, Any]
    timestamp: float


@dataclass
class NodeState:
    symbol_id: Any
    phca: PHCAState
    hermetic: HermeticState
    bayes: BayesianState
    energy: EnergyState
    mnemosyne: List[MnemosyneLogEntry] = field(default_factory=list)
    security_state: Dict[str, Any] = field(default_factory=dict)


# ---------- Simple helper metrics (runnable, but minimal) ----------

def _now() -> float:
    return time.time()


def _entropy(x: Any) -> float:
    # Very simple numeric entropy proxy
    if isinstance(x, (int, float)):
        return abs(float(x))
    if isinstance(x, dict):
        return float(len(x))
    if isinstance(x, (list, tuple, set)):
        return float(len(x))
    return 1.0


def _deviation(x: Any) -> float:
    # Placeholder deviation metric
    return _entropy(x) * 0.1


def _similarity(a: Any, b: Any) -> float:
    # Simple similarity: 1 / (1 + distance)
    if a == b:
        return 1.0
    return 0.5


def _sign(x: float) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


# ---------- PHCA extraction ----------

def extract_structure(symbol: Any) -> Dict[str, Any]:
    return {
        "raw": symbol,
        "length": len(str(symbol)),
    }


def extract_context(symbol: Any) -> Dict[str, Any]:
    return {
        "timestamp": _now(),
        "source": "sentinel_cardio",
        "hint": str(type(symbol)),
    }


def extract_semantics(symbol: Any) -> Dict[str, Any]:
    return {
        "label": str(symbol),
        "category": "generic",
    }


def extract_rhythm(symbol: Any) -> Dict[str, Any]:
    s = str(symbol)
    return {
        "periodicity": len(s),
        "flow": "steady" if len(s) > 0 else "none",
    }


def compute_phca(symbol: Any) -> PHCAState:
    P = extract_structure(symbol)
    H = extract_context(symbol)
    C = extract_semantics(symbol)
    A = extract_rhythm(symbol)
    return PHCAState(P=P, H=H, C=C, A=A)


# ---------- Hermetic layer ----------

def correspondence_metric(P: Any, C: Any, A: Any) -> float:
    return (
        _similarity(P, C) * 0.4 +
        _similarity(C, A) * 0.3 +
        _similarity(P, A) * 0.3
    )


def polarity_of(phca: PHCAState) -> Dict[str, int]:
    return {
        "P<->C": _sign(_similarity(phca.P, phca.C)),
        "C<->A": _sign(_similarity(phca.C, phca.A)),
        "P<->A": _sign(_similarity(phca.P, phca.A)),
    }


def rhythm_cycle(A: Any) -> Dict[str, Any]:
    return {
        "cycle_length": A.get("periodicity", 0),
        "phase": A.get("flow", "unknown"),
    }


def compute_hermetic(phca: PHCAState) -> HermeticState:
    HCP = correspondence_metric(phca.P, phca.C, phca.A)
    HPP = polarity_of(phca)
    HRP = rhythm_cycle(phca.A)
    return HermeticState(HCP=HCP, HPP=HPP, HRP=HRP)


# ---------- Energy model (NEE) ----------

def divergence(component: Any) -> float:
    return _entropy(component) + _deviation(component)


def compute_energy(
    phca: PHCAState,
    hermetic: HermeticState,
    risk: float,
    alpha: Dict[str, float],
) -> EnergyState:
    dP = divergence(phca.P)
    dH = divergence(phca.H)
    dC = divergence(phca.C)
    dA = divergence(phca.A)

    value = (
        alpha.get("P", 1.0) * dP +
        alpha.get("H", 1.0) * dH +
        alpha.get("C", 1.0) * dC +
        alpha.get("A", 1.0) * dA +
        alpha.get("risk", 1.0) * risk
    )

    return EnergyState(
        value=value,
        components={"dP": dP, "dH": dH, "dC": dC, "dA": dA, "risk": risk},
    )


# ---------- Bayesian layer (NEE-adjusted) ----------

def compute_likelihood(symbol: Any, phca: PHCAState, hypothesis: Any) -> float:
    # Simple alignment: if hypothesis equals label, higher score
    label = phca.C.get("label", "")
    return 0.0 if str(hypothesis) != label else 1.0


def bayes_update(
    symbol: Any,
    phca: PHCAState,
    bayes: BayesianState,
    energy: EnergyState,
) -> BayesianState:
    new_post: Dict[Any, float] = {}
    for hyp, prior in bayes.priors.items():
        prior = max(prior, 1e-9)
        likelihood = compute_likelihood(symbol, phca, hyp)
        N = likelihood + math.log(prior) - energy.value
        new_post[hyp] = N

    if not new_post:
        return BayesianState(priors=bayes.priors, posteriors={})

    maxN = max(new_post.values())
    Z = sum(math.exp(v - maxN) for v in new_post.values()) or 1.0
    for k in new_post:
        new_post[k] = math.exp(new_post[k] - maxN) / Z

    return BayesianState(priors=bayes.priors, posteriors=new_post)


# ---------- Solve et Coagula ----------

def broaden_priors(bayes: BayesianState) -> None:
    if not bayes.priors:
        return
    for k in bayes.priors:
        bayes.priors[k] = (bayes.priors[k] + 0.1) / 1.1


def sharpen_posteriors(bayes: BayesianState) -> None:
    if not bayes.posteriors:
        return
    max_key = max(bayes.posteriors, key=bayes.posteriors.get)
    for k in list(bayes.posteriors.keys()):
        if k == max_key:
            bayes.posteriors[k] *= 1.2
        else:
            bayes.posteriors[k] *= 0.8


def solve(node: NodeState) -> NodeState:
    node.energy.value *= 1.05
    broaden_priors(node.bayes)
    return node


def coagula(node: NodeState) -> NodeState:
    node.energy.value *= 0.9
    sharpen_posteriors(node.bayes)
    return node


# ---------- Mnemosyne logging ----------

def log_event(node: NodeState, event: str, metadata: Dict[str, Any]) -> None:
    entry = MnemosyneLogEntry(
        phca=node.phca,
        hermetic=node.hermetic,
        bayes=node.bayes,
        energy=node.energy,
        event=event,
        metadata=metadata,
        timestamp=_now(),
    )
    node.mnemosyne.append(entry)


# ---------- Defensive nervous system ----------

def match_signature(phca: PHCAState, signature: Any) -> bool:
    # Very simple: compare label equality if present
    label = phca.C.get("label", "")
    return str(signature) == label


def detect_anomaly(node: NodeState, dna_signatures: List[Any]) -> bool:
    return any(match_signature(node.phca, sig) for sig in dna_signatures)


def heal_node(node: NodeState) -> NodeState:
    if node.mnemosyne:
        last = node.mnemosyne[-1]
        node.phca = last.phca
        node.hermetic = last.hermetic
        node.bayes = last.bayes
        node.energy = last.energy
    return node


def revoke_keys(node: NodeState, governance_state: Dict[str, Any]) -> None:
    node.security_state["keys_revoked"] = True
    governance_state.setdefault("revocations", []).append(
        {"symbol_id": node.symbol_id, "time": _now()}
    )


# ---------- Governance / audit ----------

def audit_and_adjust(node: NodeState, governance_params: Dict[str, Any]) -> None:
    threshold = governance_params.get("energy_threshold", 100.0)
    alpha = governance_params.get("alpha", {})
    if node.energy.value > threshold:
        alpha["risk"] = alpha.get("risk", 1.0) * 1.1
        governance_params.setdefault("audit_log", []).append(
            {
                "event": "energy_exceeded",
                "symbol_id": node.symbol_id,
                "energy": node.energy.value,
                "time": _now(),
            }
        )
    governance_params["alpha"] = alpha


# ---------- Defaults ----------

def default_alpha() -> Dict[str, float]:
    return {"P": 1.0, "H": 1.0, "C": 1.0, "A": 1.0, "risk": 1.0}


def default_governance_state() -> Dict[str, Any]:
    return {
        "energy_threshold": 100.0,
        "alpha": default_alpha(),
        "audit_log": [],
        "revocations": [],
    }


# ---------- Node update loop ----------

def update_node(
    node: NodeState,
    symbol: Any,
    alpha: Dict[str, float],
    dna_signatures: List[Any],
    governance_state: Dict[str, Any],
) -> NodeState:
    node.phca = compute_phca(symbol)
    node.hermetic = compute_hermetic(node.phca)
    risk = 0.0  # placeholder risk
    node.energy = compute_energy(node.phca, node.hermetic, risk, alpha)
    node.bayes = bayes_update(symbol, node.phca, node.bayes, node.energy)

    if detect_anomaly(node, dna_signatures):
        log_event(node, "anomaly_detected", {"symbol": symbol})
        node = heal_node(node)
        revoke_keys(node, governance_state)

    node = solve(node)
    node = coagula(node)
    audit_and_adjust(node, governance_state)
    log_event(node, "update_complete", {"symbol": symbol})
    return node
