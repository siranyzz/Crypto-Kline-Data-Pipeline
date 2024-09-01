# Crypto Kline Data Pipeline

This project is a simple data pipeline that fetches cryptocurrency Kline (candlestick) data from the Binance API, stores it in a local database, and processes it into a structured format. The pipeline is designed to fetch data in 1-minute intervals and is divided into three stages: Bronze (raw data), Silver (cleaned data), and Gold (aggregated/processed data).

## Project Structure

- **createDB.py**: Creates the SQLite database and tables for storing Kline data.
- **get_klines.py**: Fetches Kline data from the Binance API and stores it in the Bronze layer.
- **silver_layer_ingestion.py**: Processes and cleans the data from the Bronze layer and inserts it into the Silver layer.
- **main.py**: The main entry point of the pipeline, orchestrating the data fetching and processing.

## Setup Instructions

### 1. Install Required Packages

Ensure you have Python installed. Then, install the required packages using pip:

```bash
pip install pandas sqlite3 binance connector

** Setup Binance API Keys
You need to set up your Binance API keys to fetch data from the Binance API. Follow the https://www.binance.com/en-NG/support/faq/how-to-create-api-keys-on-binance-360002502072 to create your API keys.
```
