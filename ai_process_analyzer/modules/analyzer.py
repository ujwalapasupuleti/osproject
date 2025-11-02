import pandas as pd

def detect_anomalies(df):
    if df.empty:
        return pd.DataFrame()
    df['z_cpu'] = (df['cpu_percent'] - df['cpu_percent'].mean()) / df['cpu_percent'].std(ddof=0)
    anomalies = df[df['z_cpu'].abs() > 2]
    return anomalies[['pid', 'name', 'cpu_percent', 'z_cpu']]

def identify_bottlenecks(df):
    high_cpu = df[df['cpu_percent'] > 50].sort_values(by='cpu_percent', ascending=False)
    high_mem = df[df['memory_percent'] > 30].sort_values(by='memory_percent', ascending=False)
    return high_cpu, high_mem
