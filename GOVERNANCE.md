# Governance Protocol – Sentinel Cardio Integrity Tokens

## Purpose

This document defines the **access control, roles, and operational rules** for the Sentinel Cardio Integrity Tokens (SNTR). It ensures that tokens – which certify the coherence of biological, forensic, or public records data – are only accessible to authorized parties while remaining publicly verifiable for authenticity.

## Core Principles

1. **Least Privilege** – No role has more access than strictly necessary.  
2. **Immutable Audit Trail** – Every access or delegation attempt is logged in the Exhibit A Manifest.  
3. **Revocable Delegation** – The First Keeper can revoke any delegated access at any time.  
4. **No Anonymous Mapping** – Raw data (e.g., genomic hashes) are never publicly linked to token holders’ identities.

## Roles & Permissions

| Role | Description | Permissions |
|------|-------------|--------------|
| **First Keeper** | Anthony Jordan Blair (creator & sovereign architect) | Full: mint tokens, revoke tokens, delegate access, view all token metadata, update governance rules |
| **Verified Lineage** | Immediate family members (as designated in writing, sealed in Exhibit A) | Read‑only: view tokens associated with their own genetic or medical records |
| **Clinical / Forensic Auditor** | Third‑party auditor under contract | Query: verify a token’s signature and timestamp for a specific sample ID; cannot list all tokens or map to identities |
| **Public (Verifier)** | Any anonymous entity | Validate: check token signature, timestamp, and linked data hash – no identity mapping |

## Access Workflow

### Minting a New Token (First Keeper only)

1. Engine computes SCI ≥ 0.85.  
2. First Keeper signs the token with HSM‑protected private key.  
3. Token is written to the ledger (local JSON + optional blockchain).  
4. An immutable log entry is created in `Exhibit_A_Manifest.json`.

### Delegating Access to a Lineage Member

1. First Keeper creates a signed delegation record:  
   `{ "lineage_member_public_key": "<key>", "scope": "own_tokens", "expires": "<timestamp>" }`  
2. Record is stored in the `governance/` folder (encrypted at rest).  
3. Lineage member can now query tokens linked to their own identifier.

### Auditing a Specific Token

Any auditor with a valid contract can submit a token ID to the verification API.  
The API returns:
- Token validity (true/false)
- Timestamp of minting
- SCI value
- Hash of the source data (not the raw data itself)

The auditor cannot list all tokens or correlate across samples.

### Public Verification

Anyone can run:
```bash
python verify_token.py --token <token_id>