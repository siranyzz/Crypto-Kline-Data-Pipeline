import pandas as pd
import sqlite3
from datetime import datetime
#  file_path = f'bronze/{current_date}/BTCUSDT_{current_date}_klines.csv'
def silver_layer_ingestion(file_path,date):
    # Connect to the SQLite database (creates a new one if it doesn't exist)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()


    current_date = date
   

    # Read data from the Bronze layer
    df = pd.read_csv(file_path)

    # Add a date column
    df['ingested_date_aus_time'] = current_date



    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')
    # Clean and transform the data
    df_cleaned = df[df['Volume'] > 0].copy()

    # Rename columns to match the database table field names
    df_cleaned = df_cleaned.rename(columns={
        'Open time': 'open_time',
        'Close time': 'close_time',
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Volume': 'volume',
        'Quote asset volume': 'quote_asset_volume',
        'Number of trades': 'number_of_trades',
        'Taker buy base asset volume': 'taker_buy_base_asset_volume',
        'Taker buy quote asset volume': 'taker_buy_quote_asset_volume'
    })
    # Drop the 'Ignore' column
    df_cleaned = df_cleaned.drop(columns=['Ignore'])


    # Insert the cleaned data into the Silver layer
    df_cleaned.to_sql('silver_klines', conn, if_exists='append', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    print(f"Data from {current_date} has been cleaned and inserted into the Silver layer.")
