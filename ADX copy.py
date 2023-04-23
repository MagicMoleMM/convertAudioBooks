import talib
import pandas as pd
import numpy as np
import requests
import json

# Define the input parameters
length = 14
threshold = 20

# Define the function to calculate ADX and DI
def calculate_adx_di(df):
    high = df['high'].values
    low = df['low'].values
    close = df['close'].values

    # Calculate TrueRange
    tr = talib.TRANGE(high, low, close)

    # Calculate Directional Movement
    dm_plus = np.where(high[1:] - high[:-1] > low[:-1] - low[1:], high[1:] - high[:-1], 0)
    dm_minus = np.where(low[:-1] - low[1:] > high[1:] - high[:-1], low[:-1] - low[1:], 0)

    # Calculate Smoothed TrueRange and Directional Movement
    atr = talib.SMA(tr, length)
    dm_plus_smooth = talib.SMA(dm_plus, length)
    dm_minus_smooth = talib.SMA(dm_minus, length)

    # Calculate Directional Index (DI)
    di_plus = dm_plus_smooth / atr * 100
    di_minus = dm_minus_smooth / atr * 100

    # Calculate Directional Index Difference (DX)
    dx = np.abs(di_plus - di_minus) / (di_plus + di_minus) * 100

    # Calculate ADX
    adx = talib.SMA(dx, length)

    return di_plus, di_minus, adx

# Retrieve the historical data
symbol = 'AAPL'
interval = '1h'
limit = 200
url = f'https://api.binance.com/api/v3/klines?symbol={symbol}USDT&interval={interval}&limit={limit}'
response = requests.get(url)
df = pd.DataFrame(json.loads(response.text))
df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# Calculate ADX and DI
di_plus, di_minus, adx = calculate_adx_di(df)

# Plot the results
import matplotlib.pyplot as plt

plt.plot(di_plus, label='DI+')
plt.plot(di_minus, label='DI-')
plt.plot(adx, label='ADX')
plt.axhline(y=threshold, color='gray', linestyle='--')
plt.legend()
plt.show()


