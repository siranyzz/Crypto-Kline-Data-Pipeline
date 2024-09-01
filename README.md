# Crypto Kline Data Pipeline

This project is a simple data pipeline that fetches cryptocurrency Kline (candlestick) data from the Binance API, stores it in a local database, and processes it into a structured format. The pipeline is designed to fetch data in 1-minute intervals and is divided into three stages: Bronze (raw data), Silver (cleaned data), and Gold (aggregated/processed data).

## Architecture

The following diagram illustrates the architecture of the pipeline:

![Architecture Diagram](https://github.com/siranyzz/Crypto-Kline-Data-Pipeline/blob/main/1725210178503.jpg)

## Project Structure

- **createDB.py**: Creates the SQLite database and tables for storing Kline data.
- **get_klines.py**: Fetches Kline data from the Binance API and stores it in the Bronze layer.
- **silver_layer_ingestion.py**: Processes and cleans the data from the Bronze layer and inserts it into the Silver layer.
- **main.py**: The main entry point of the pipeline, orchestrating the data fetching and processing.

## Setup Instructions

### 1. Install Required Packages

Ensure you have Python installed. Then, install the required packages using pip:

```bash
pip install pandas sqlite3 binance-connector
```
### 2.Setup Binance API Keys
You need to set up your Binance API keys to fetch data from the Binance API.Follow the instructions [here](https://www.binance.com/en-NG/support/faq/how-to-create-api-keys-on-binance-360002502072) to create your API keys.
 to create your API keys.
```json
{
    "api_key": "your_api_key_here",
    "secret_key": "your_secret_key_here"
}
```
### 3. Create the Database
Run the createDB.py script to create the SQLite database and tables:
```bash
python createDB.py
```
### 4. Fetch and Process Kline Data
```bash
python main.py
```
This will:

Fetch the Kline data for the current date from the Binance API and save it to the Bronze layer.
Clean and process the data, and then insert it into the Silver layer.
The gold layer is created by a view, which is already in the DB.

### 5. Customize Date
If you want to fetch and process data for a specific date, you can modify the current_date variable in main.py. The format should be YYYY-MM-DD.

## How the Pipeline Works
**1.Bronze Layer (Raw Data)**: The get_klines.py script fetches 1-minute interval Kline data from the Binance API and saves it as a CSV file in the Bronze layer. The file is named in the format BTCUSDT_<date>_klines.csv.

**2.Silver Layer** (Cleaned Data): The silver_layer_ingestion.py script reads the data from the Bronze layer, cleans it (removing unnecessary columns and filtering out records with zero volume), and then inserts the cleaned data into the Silver layer of the SQLite database.

**3.Gold Layer** (Aggregated Data): The Gold layer is implemented as a SQL view that aggregates and processes data from the Silver layer, making it ready for analysis and reporting.

## Future Improvements
**Cloud Deployment**: Deploy the entire pipeline to cloud services like AWS, GCP, or Azure for scalability and robustness.

**Scheduled Automation**: Use tools like Apache Airflow to automate and schedule the pipeline execution, enabling regular data ingestion and processing.

**Expand Data Handling**: Extend the pipeline to handle multiple cryptocurrency pairs and different time intervals.

## Key Considerations
### 1. Select a Suitable API and Describe Why It Was Chosen
**API Chosen**: The Binance API was selected because it provides comprehensive and reliable access to real-time and historical cryptocurrency market data, including Kline (candlestick) data. This API is particularly suitable for this project due to its robustness, the variety of supported time intervals, and the extensive documentation available.
### 2. Implement the Data Ingestion Process to Pull Daily Data and Ensure the Process Is Automated
The data ingestion process is implemented in the **get_klines.py** script, which fetches Kline data for a specific symbol (e.g., BTC/USDT) and stores it in the Bronze layer as a CSV file. The ingestion process is designed to be automated by running the **main.py** script daily, either manually or via a scheduling tool like cron or Apache Airflow.
### 3.Use Appropriate Data Storage and Data Formats
**Data Storage**: The project uses a local SQLite database for storing processed (Silver layer) data and local filesystem storage for raw (Bronze layer) data.

**Data Format**:

   **Bronze Layer**: Data is stored as CSV files. CSV was chosen because it is human-readable, easy to work with in Python (via pandas), and sufficient for storing tabular data with a moderate volume.
 
   **Silver Layer**: Data is stored in SQLite, a lightweight relational database, which is ideal for managing structured data with the need for querying and processing.
   
**Alternatives Considered**:

**Parquet**: While Parquet is efficient for large-scale data storage, especially in columnar format, it was discarded for this project due to its overhead in setting up for smaller datasets and the simplicity needed in this pipeline.

**JSON**: JSON could have been used for raw data storage due to its flexibility, but CSV was preferred for its simplicity and better integration with pandas for tabular data.

**Cloud Storage**: Cloud storage solutions like AWS S3 were considered but not implemented due to the local scope of this project. This could be revisited for larger-scale deployments.
 
