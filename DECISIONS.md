# DECISIONS.md

# Major Product Decisions

## 1. SAP Data Handling

I chose CSV-based SAP ingestion instead of direct SAP integration.

Reason:
- SAP systems vary heavily between organizations.
- CSV exports are common operational workflows.
- Easier to prototype realistically.

Handled subset:
- Fuel procurement
- Fuel quantity
- Natural gas consumption

Ignored:
- Complex SAP IDoc structures
- Real-time SAP APIs
- Vendor reconciliation

---

## 2. Utility Data Design

I chose utility CSV exports.

Reason:
- Facilities teams commonly download CSVs from portals.
- Faster analyst workflow.
- Easier manual verification.

Handled:
- Meter readings
- Electricity consumption
- Invalid negative readings

Ignored:
- Tariff calculations
- Time-of-use pricing
- Multi-meter reconciliation

---

## 3. Travel Data Design

I modeled travel records using distance-based entries.

Reason:
- Real travel systems often expose airport routes and trip distances.
- Emissions depend on travel category.

Handled:
- Flights
- Hotels
- Ground transport

Ignored:
- Automatic emissions factor calculation
- Multi-currency expense normalization
- Real Concur/Navan OAuth integration

---

## 4. Review Workflow

I added:
- APPROVE
- FLAG

Reason:
Human review is important before ESG audit locking.

---

## 5. Frontend Choice

React was chosen because:
- Fast dashboard rendering
- Component-based UI
- Easy API integration with Django REST