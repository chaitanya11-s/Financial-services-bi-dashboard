# Business Requirements Document (BRD)
## Financial Performance & Operations Dashboard

### 1. Executive Summary
The goal is to transition from manual spreadsheet-based reporting to an automated Business Intelligence dashboard. This dashboard will provide daily insights into Portfolio Performance, Operational Efficiency, and Sales Metrics for the Executive Leadership Team (ELT) and Desk Heads.

### 2. Stakeholder Requirements

#### 2.1 Head of Trading (Portfolio Performance)
- **Requirement**: "I need to see daily returns broken down by asset class to identify underperforming sectors immediately."
- **KPI**: `Daily Return %`, `Sharpe Ratio` (Rolling 30-day), `Total AUM` (Assets Under Management).
- **Visualization**: Trend lines for AUM growth, Heatmap of returns by Asset Class.

#### 2.2 Operations Manager (Operational Efficiency)
- **Requirement**: "We are seeing too many failed trades. I need to track settlement errors daily to pinpoint which portfolios are causing bottlenecks."
- **KPI**: `Settlement Error Rate` (Errors / Total Trades), `Efficiency Score` (Weighted metric).
- **Visualization**: Bar chart of errors by Portfolio, Gauge chart for overall Efficiency Score.

#### 2.3 Head of Sales (Sales Distribution)
- **Requirement**: "Which channels are driving the most AUM growth? We need to allocate resources effectively."
- **KPI**: `Net New Money` (AUM Inflow), `Conversion Rate`.
- **Visualization**: Pie chart of AUM Inflow by Channel.

### 3. Data Sources & Automation
- **Input**: Daily CSV exports from the Trading System (simulated).
- **Process**: Automated Python script (`daily_ingestion_job`) cleanses data, calculates KPIs, and loads into the Data Warehouse.
- **Output**: Tableau Dashboard connected to the Data Warehouse.
