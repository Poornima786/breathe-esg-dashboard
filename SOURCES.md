# SOURCES.md

# Source Research

## 1. SAP Procurement and Fuel Data

### Research
Reviewed common SAP export formats including:
- CSV exports
- IDoc structures
- OData services

### Chosen Format
CSV export.

### Why
Most operational teams export SAP reports as spreadsheets or CSVs for analyst review.

### Realistic Characteristics
- Inconsistent units
- Fuel categories
- Plant-level procurement entries

### Sample Data
Includes:
- Diesel procurement
- Petrol procurement
- Natural gas consumption

### Real Deployment Risks
- SAP custom schemas differ between companies
- Localization issues
- Missing plant mappings

---

## 2. Utility Electricity Data

### Research
Reviewed utility portal exports and electricity billing formats.

### Chosen Format
CSV portal export.

### Why
Facilities teams commonly use downloadable reports.

### Realistic Characteristics
- Meter IDs
- Consumption values
- Billing anomalies

### Sample Data
Includes:
- Plant electricity meter
- Head office consumption
- Invalid negative meter reading

### Real Deployment Risks
- Different utility schemas
- Billing period mismatches
- Unit inconsistencies

---

## 3. Corporate Travel Data

### Research
Reviewed travel management platforms:
- Concur
- Navan

### Chosen Format
CSV travel export.

### Why
Travel teams often export expense/travel reports manually.

### Realistic Characteristics
- Flight routes
- Hotel nights
- Ground transport distances

### Sample Data
Includes:
- Delhi to Mumbai Flight
- Bangalore Hotel Stay
- Pune to Mumbai Cab

### Real Deployment Risks
- Missing travel distances
- Currency normalization
- Duplicate trip entries