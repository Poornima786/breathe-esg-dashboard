# Breathe ESG Dashboard

A prototype ESG data ingestion and review platform built using Django REST Framework and React.

## Live Demo

Frontend:
https://breathe-esg-dashboard-jade.vercel.app

Backend API:
https://breathe-esg-dashboardd.onrender.com/api/records/

## Features

- CSV ingestion for:
  - SAP fuel/procurement data
  - Utility electricity data
  - Corporate travel data

- Analyst review dashboard
- Approve / Flag workflow
- Automatic suspicious value detection
- Scope categorization
- Audit source tracking
- Emission visualization charts
- Duplicate upload prevention

## Tech Stack

### Backend
- Django
- Django REST Framework
- SQLite

### Frontend
- React
- Vite
- Recharts

### Deployment
- Render (Backend)
- Vercel (Frontend)

## Sample Data Sources

### SAP
Simulated flat-file fuel procurement export.

### Utility
Electricity consumption CSV export from utility portal.

### Travel
Corporate travel export inspired by Concur/Navan formats.

## Project Structure

backend/
frontend/
MODEL.md
DECISIONS.md
TRADEOFFS.md
SOURCES.md

## Key Decisions

- Prototype focused on ingestion and analyst review workflow
- Scope categorization mapped automatically
- Negative values automatically flagged
- Duplicate uploads prevented using source/value checks

## Tradeoffs

- No real emissions factor calculations
- Simplified tenant model
- CSV-only ingestion for prototype scope

## Made By

Poornima Srivastava