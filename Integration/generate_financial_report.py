
import sys
import os

# Add parent directory to path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from financial_kpi_module import FinancialKPICalculator

def main():
    print("Starting Financial Data Pipeline Used for BI Dashboarding...")
    
    # Initialize Calculator
    calculator = FinancialKPICalculator()
    
    # 1. Load Data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, '../financial_datasets/portfolio_data.csv')
    print(f"Loading data from {input_file}...")
    try:
        calculator.load_data(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please run generate_data.py first.")
        return

    # 2. Calculate KPIs
    print("Calculating Business Metrics (Efficiency Score, Risk-Adjusted Returns)...")
    calculator.calculate_kpis()
    
    # 3. Generate Reports
    output_file = 'financial_kpi_report.csv'
    print(f"Exporting processed data for Tableau to {output_file}...")
    calculator.export_to_sql_format(output_file)
    
    # 4. Summary Preview
    print("\n--- Daily Summary Preview (Top 5 rows) ---")
    summary = calculator.get_summary_report()
    print(summary.head())
    print("------------------------------------------")
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
