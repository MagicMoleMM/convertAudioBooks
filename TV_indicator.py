import ta
import math
from typing import Union
import numpy as np

# indicator parameters
lower_tf = '1'
bars_in_tf = 100
step_in_tf = 1
usewa = True
waveALength = 55
len = 14
th = 20

# function to calculate balanced volume
def balanced_volume(open: np.ndarray, close: np.ndarray, volume: np.ndarray, range_1: int) -> np.ndarray:
    vol = np.full_like(volume, np.nan)
    for i in range(range_1):
        if open[i] == close[i]:
            vol[i] = volume[i] if np.isnan(vol[i]) else vol[i] + volume[i]
    return vol

# function to calculate buying volume
def buying_volume(open: np.ndarray, close: np.ndarray, volume: np.ndarray, range_2: int) -> np.ndarray:
    vol = np.full_like(volume, np.nan)
    for i in range(range_2):
        if open[i] < close[i]:
            vol[i] = volume[i] if np.isnan(vol[i]) else vol[i] + volume[i]
    return vol

# function to calculate selling volume
def selling_volume(open: np.ndarray, close: np.ndarray, volume: np.ndarray, range_3: int) -> np.ndarray:
    vol = np.full_like(volume, np.nan)
    for i in range(range_3):
        if open[i] > close[i]:
            vol[i] = volume[i] if np.isnan(vol[i]) else vol[i] + volume[i]
    return vol

# request data from TradingView
symbol = 'BTCUSDT'
timeframe = '15'
ohlcv = binance.fetch_ohlcv(symbol, timeframe)
open = ohlcv[:, 1]
high = ohlcv[:, 2]
low = ohlcv[:, 3]
close = ohlcv[:, 4]
volume = ohlcv[:, 5]
ts = ohlcv[:, 0] // 1000

lower_buy_vol = buying_volume(open, close, volume, bars_in_tf)
lower_sell_vol = selling_volume(open, close, volume, bars_in_tf)
balanced_vol = balanced_volume(open, close, volume, bars_in_tf)

# get_buy and get_sell
get_buy = np.zeros_like(lower_buy_vol)
get_sell = np.zeros_like(lower_sell_vol)
for i in range(bars_in_tf):
    if lower_buy_vol[i] > lower_buy_vol[i-1] and lower_buy_vol[i] > lower_sell_vol[i]:
        get_buy[i] = lower_buy_vol[i]
    else:
        get_buy[i] = get_buy[i-1]

    if lower_sell_vol[i] > lower_sell_vol[i-1] and lower_sell_vol[i] > lower_buy_vol[i]:
        get_sell[i] = lower_sell_vol[i]
    else:
        get_sell[i] = get_sell[i-1]

# Wave A
ema_1 = ta.ema(close, 8)
fastMA1 = ema_1 if usewa else np.nan
ema_2 = ta.ema(close, waveALength)
slowMA1 = ema_2 if usewa else np.nan
macd1 = fastMA1 - slowMA1 if usewa else np.nan
ema_3 = ta.ema(macd1, waveALength)
signal1 = ema_3 if usewa else np.nan
histA = macd1 - signal1 if usewa else np.nan

