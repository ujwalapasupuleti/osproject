import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def forecast_cpu(df):
    if df.empty:
        return None
    df = df.groupby('timestamp')['cpu_percent'].mean().reset_index()
    df['t'] = np.arange(len(df))
    X, y = df[['t']], df['cpu_percent']

    model = LinearRegression()
    model.fit(X, y)

    future_t = np.arange(len(df), len(df) + 5).reshape(-1, 1)
    pred = model.predict(future_t)
    timestamps = [df['timestamp'].iloc[-1] + timedelta(seconds=i + 1) for i in range(5)]

    forecast_df = pd.DataFrame({'timestamp': timestamps, 'predicted_cpu': pred})
    return forecast_df
