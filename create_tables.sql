CREATE TABLE IF NOT EXISTS silver_klines (
    ingested_date_aus_time TEXT,  
    open_time TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume REAL,
    close_time TEXT,
    quote_asset_volume REAL,
    number_of_trades INTEGER,
    taker_buy_base_asset_volume REAL,
    taker_buy_quote_asset_volume REAL
);


CREATE VIEW IF NOT EXISTS gold_daily_summary AS
SELECT
    DATE(open_time) AS date,                     
    MIN(open_time) AS first_open_time,           
    MAX(close_time) AS last_close_time,          
    FIRST_VALUE(open) OVER (PARTITION BY DATE(open_time) ORDER BY open_time) AS open,  
    MAX(high) AS high,                           
    MIN(low) AS low,                             
    LAST_VALUE(close) OVER (PARTITION BY DATE(open_time) ORDER BY close_time ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS close,  -- 当天的收盘价
    SUM(volume) AS volume                        
FROM
    silver_klines
GROUP BY
    DATE(open_time);