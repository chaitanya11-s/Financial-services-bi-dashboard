-- Financial Services BI Dashboard Schema

DROP TABLE IF EXISTS portfolio_performance;
CREATE TABLE portfolio_performance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report_date DATE,
    portfolio_id VARCHAR(20),
    asset_class VARCHAR(50),
    market_value DECIMAL(15, 2),
    daily_return DECIMAL(10, 6)
);

DROP TABLE IF EXISTS operational_metrics;
CREATE TABLE operational_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report_date DATE,
    portfolio_id VARCHAR(20),
    trades_count INT,
    settlement_errors INT,
    compliance_checks_flag BOOLEAN
);

DROP TABLE IF EXISTS sales_metrics;
CREATE TABLE sales_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report_date DATE,
    channel VARCHAR(50),
    new_accounts INT,
    aum_inflow DECIMAL(15, 2)
);
