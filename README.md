# Financial Services BI Dashboard

![Dashboard Preview](images/dashboard_preview_v2.png)

## Overview
This project focuses on **Automated Business Intelligence** for Asset Management. 

The goal was to replace manual Excel-based reporting with a Python + Tableau pipeline. It processes daily portfolio data to track:
- **Performance**: Returns, AUM, and Risk metrics.
- **Operations**: Settlement efficiency and compliance flags.
- **Sales**: Net new money flows by channel.

## Architecture
1. **Data Ingestion**: Python script (`Integration/generate_financial_report.py`) reads raw trade logs.
2. **KPI Engine**: Custom logic in `financial_kpi_module.py` computes business metrics (e.g., Efficiency Score, Risk-Adj Return).
3. **Storage**: Schema designed for SQL warehousing (`SQL Database Schemas/financial_schema.sql`).
4. **Visualization**: Tableau dashboard for specific stakeholder views (Trading, Ops, Sales).

## Usage
### 1. Requirements
```bash
pip install pandas numpy
```

### 2. Run the Pipeline
Generate fresh data (if needed):
```bash
python generate_data.py
```

Run the ETL job:
```bash
python Integration/generate_financial_report.py
```

This outputs `financial_kpi_report.csv` which feeds the Tableau dashboard.

## Project Structure
- `financial_kpi_module.py`: Core business logic.
- `business_requirements/`: Notes on stakeholder needs.
- `SQL Database Schemas/`: DDL for the data warehouse tables.
- `Tableau Files/`: Documentation and setup guides.
