# MODEL.md

## Data Model Design

The system uses a centralized `EmissionRecord` model to normalize ESG data coming from multiple external sources.

## Core Fields

### source_type
Identifies where the record originated from.

Supported values:
- SAP
- UTILITY
- TRAVEL

This supports source-of-truth tracking and auditing.

---

### source_name
Human-readable description of the activity.

Examples:
- Diesel Procurement
- Plant Electricity Meter
- Delhi to Mumbai Flight

---

### value
Stores the numeric activity value.

Examples:
- Fuel quantity
- Electricity consumption
- Travel distance

Stored as FloatField to support decimal values.

---

### unit
Stores normalized measurement units.

Examples:
- Litres
- kWh
- km
- nights

Normalization is important because source systems provide inconsistent formats.

---

### status
Tracks analyst review lifecycle.

Supported states:
- PENDING
- APPROVED
- FLAGGED

This enables human review before audit lock.

---

### uploaded_at
Timestamp for ingestion tracking and audit history.

---

### original_file
Stores uploaded source filename for traceability.

---

# Multi-Tenancy Design

The current prototype is single-tenant.

For production:
- Add Organization model
- Add ForeignKey from EmissionRecord → Organization
- Scope all queries per organization

---

# Scope Categorization

Future production version would include:
- Scope 1
- Scope 2
- Scope 3

Examples:
- Fuel combustion → Scope 1
- Purchased electricity → Scope 2
- Business travel → Scope 3

---

# Audit Trail

Current prototype stores:
- upload timestamp
- source filename
- review status

Production version should additionally track:
- reviewer identity
- edit history
- approval timestamps
- immutable audit logs