import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_financial_data(num_rows=1000):
    np.random.seed(42)
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(num_rows)]
    
    portfolio_ids = ['PF_001', 'PF_002', 'PF_003', 'PF_004', 'PF_005']
    asset_classes = ['Equities', 'Fixed Income', 'Derivatives', 'Commodities', 'Real Estate']
    client_segments = ['Institutional', 'High Net Worth', 'Retail', 'Corporate']
    
    data = []
    
    for date in dates:
        # Generate data for a few random portfolios each day
        for _ in range(5): 
            pf_id = random.choice(portfolio_ids)
            asset_class = random.choice(asset_classes)
            segment = random.choice(client_segments)
            
            market_value = np.random.normal(1000000, 200000)
            daily_return = np.random.normal(0.0005, 0.015)
            trades_count = np.random.randint(5, 50)
            transaction_volume = trades_count * np.random.uniform(1000, 50000) # New: Volume
            settlement_errors = np.random.poisson(0.5)
            compliance_checks = np.random.choice([0, 1], p=[0.98, 0.02])
            
            # New Metrics for Resume
            client_retention_flag = np.random.choice([1, 0], p=[0.95, 0.05]) # 1=Retained, 0=Churned
            nps_score = np.random.randint(1, 11) # Net Promoter Score
            liquidity_ratio = np.random.uniform(0.5, 3.0) 
            expenses = np.random.uniform(500, 5000)
            
            data.append([
                date.strftime('%Y-%m-%d'),
                pf_id,
                asset_class,
                segment,
                round(market_value, 2),
                round(daily_return, 6),
                trades_count,
                round(transaction_volume, 2),
                settlement_errors,
                compliance_checks,
                client_retention_flag,
                nps_score,
                round(liquidity_ratio, 2),
                round(expenses, 2)
            ])
            
    columns = [
        'Date', 'Portfolio_ID', 'Asset_Class', 'Client_Segment', 'Market_Value', 
        'Daily_Return', 'Trades_Count', 'Transaction_Volume', 'Settlement_Errors', 
        'Compliance_Checks', 'Client_Retention_Flag', 'NPS_Score', 'Liquidity_Ratio', 'Expenses'
    ]
    
    df = pd.DataFrame(data, columns=columns)
    return df

if __name__ == "__main__":
    df = generate_financial_data(700) # Approx 2 years of data
    df.to_csv('financial_datasets/portfolio_data.csv', index=False)
    print("Financial data generated: financial_datasets/portfolio_data.csv")
