from binance.spot import Spot
import json
import pandas as pd
import os
from datetime import datetime

def get_klines(api_location,output_directory,date):
    with open(api_location, 'r') as file:
        config = json.load(file)

    api_key = config['api_key']
    api_secret = config['secret_key']


    client = Spot(api_key=api_key, api_secret=api_secret)


    symbol = 'BTCUSDT'
    interval = '1m'
    current_date = date
    start_time = int(datetime.strptime(current_date, '%Y-%m-%d').timestamp() * 1000)
    end_time = start_time + 24 * 60 * 60 * 1000 - 1  # Full day in milliseconds


    klines = client.klines(symbol=symbol, interval=interval, startTime=start_time, endTime=end_time)


    columns = [
        'Open time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close time', 'Quote asset volume', 'Number of trades',
        'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'
    ]


    df = pd.DataFrame(klines, columns=columns)



    directory = f'{output_directory}/{current_date}/'
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, f'{symbol}_{current_date}_klines.csv')
    df.to_csv(file_path, index=False)
    return file_path

