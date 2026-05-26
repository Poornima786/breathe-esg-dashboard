# TRADEOFFS.md

# Deliberate Tradeoffs

## 1. No Authentication System

I intentionally skipped login/authentication.

Reason:
- Assignment focus was ingestion and review workflow.
- Time prioritized toward realistic source handling.

Production system would require:
- RBAC
- SSO
- Analyst permissions

---

## 2. No Real SAP/API Integrations

I used CSV uploads instead of live enterprise integrations.

Reason:
- Real SAP integrations are highly organization-specific.
- Prototype goal was demonstrating ingestion logic.

Production would require:
- SAP OData
- SFTP ingestion
- OAuth-secured APIs

---

## 3. No Advanced Emission Calculations

The prototype stores activity data only.

Reason:
- Focused on ingestion normalization and analyst workflow.
- Emission factor libraries add significant complexity.

Production would require:
- Regional emission factors
- Versioned calculation methodology
- Audit-safe factor tracking