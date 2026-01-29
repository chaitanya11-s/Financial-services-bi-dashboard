# Tableau Dashboard Setup Notes

Steps to recreate the dashboard from the `financial_kpi_report.csv` output.

## 1. Data Connection
1. Connect to Text File -> `financial_kpi_report.csv`.


## 2. Verify Data Types
Ensure Tableau reads the columns correctly:
- **Date**: Change to `Date` property.
- **Daily_Return**, **Market_Value**, **Efficiency_Score**: Ensure these are `Measure (Decimal)`.
- **Portfolio_ID**, **Asset_Class**: Ensure these are `Dimension (String)`.

## 3. Build Dashboard Views

### View 1: Portfolio Performance (Head of Trading)
*Goal: Visualize returns and AUM growth.*
1. **Sheet Name**: "Daily Returns by Asset Class"
2. **Columns**: `Date` (Day/Month).
3. **Rows**: `AVG(Daily_Return)`.
4. **Color**: `Asset_Class`.
5. **Chart Type**: Line Chart.
6. **Insight**: Look for spikes or drops to identify volatile asset classes.

### View 2: Operational Efficiency (Ops Manager)
*Goal: Track settlement errors.*
1. **Sheet Name**: "Efficiency Score Gauge"
2. **Rows**: `AVG(Efficiency_Score)`.
3. **Columns**: `Portfolio_ID`.
4. **Filters**: Add `Efficiency_Score` to filters (Color code: Red < 95, Green > 98).
5. **Chart Type**: Bar Chart or Bullet Graph.

### View 3: Risk Analysis (Compliance)
*Goal: Identify underperforming assets.*
1. **Sheet Name**: "Risk Matrix"
2. **Columns**: `Asset_Class`.
3. **Rows**: `Performance_Category`.
4. **Text/Label**: `Count(Portfolio_ID)`.
5. **Chart Type**: Highlight Table / Heatmap.

## 4. Final Dashboard Assembly
1. Create a **New Dashboard** tab.
2. Drag all 3 sheets onto the canvas.
3. Add a title: "Daily Financial Operations Report".
4. Add a "Date Range" filter and apply it to **All Worksheets**.

## 5. Publish
- Save as `.twbx` (Tableau Packaged Workbook) to include the data.
- Publish to Tableau Public for your portfolio.
