import pandas as pd
import numpy as np

def adx_di(df, len=14, th=20):
    true_range = pd.DataFrame({
        'high': df['high'],
        'low': df['low'],
        'close': df['close'].shift(1)
    }).apply(lambda x: max(
        x['high']-x['low'],
        abs(x['high']-x['close']),
        abs(x['low']-x['close'])
    ), axis=1)
    directional_movement_plus = np.where(
        (df['high']-df['high'].shift(1)) > (df['low'].shift(1)-df['low']),
        np.maximum(df['high']-df['high'].shift(1), 0),
        0
    )
    directional_movement_minus = np.where(
        (df['low'].shift(1)-df['low']) > (df['high']-df['high'].shift(1)),
        np.maximum(df['low'].shift(1)-df['low'], 0),
        0
    )
    smoothed_true_range = true_range.rolling(window=len).mean()
    smoothed_directional_movement_plus = directional_movement_plus.rolling(window=len).mean()
    smoothed_directional_movement_minus = directional_movement_minus.rolling(window=len).mean()
    di_plus = (smoothed_directional_movement_plus / smoothed_true_range) * 100
    di_minus = (smoothed_directional_movement_minus / smoothed_true_range) * 100
    dx = (np.abs(di_plus - di_minus) / (di_plus + di_minus)) * 100
    adx = dx.rolling(window=len).mean()
    return pd.DataFrame({
        'di_plus': di_plus,
        'di_minus': di_minus,
        'adx': adx
    })

# Example usage:
df = pd.read_csv('example.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
result = adx_di(df)

