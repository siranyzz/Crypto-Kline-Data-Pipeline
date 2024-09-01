from  get_klines import get_klines
from silver_layer_ingestion import silver_layer_ingestion
from datetime import datetime


api_location = 'binance_api.json'
output_directory = 'bronze'
current_date = datetime.now().strftime('%Y-%m-%d')

def main():
    # Define the paths for API keys and output directory
    api_location = 'binance_api.json'
    output_directory = 'bronze'
    bronze_file_path=get_klines(api_location, output_directory,current_date)
    silver_layer_ingestion(bronze_file_path,current_date)

if __name__ == "__main__":
    main()