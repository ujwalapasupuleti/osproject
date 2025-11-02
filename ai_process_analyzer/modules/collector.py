import psutil
import pandas as pd
from datetime import datetime

def collect_metrics():
    records = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            info['timestamp'] = datetime.now()
            records.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    df = pd.DataFrame(records)
    return df
