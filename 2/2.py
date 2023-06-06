import pandas as pd
import numpy as np
from scipy.stats import zscore


data = {
    'date': pd.date_range(start='01-01-2020', periods=100),
    'sessions': np.random.randint(50, 200, size=100),
    'new_users': np.random.randint(1, 50, size=100),
    'session_time': np.random.randint(5, 15, size=100)
}
df = pd.DataFrame(data)


df['sessions_zscore'] = zscore(df['sessions'])
df['new_users_zscore'] = zscore(df['new_users'])
df['session_time_zscore'] = zscore(df['session_time'])


df['sessions_anomaly'] = np.where(np.abs(df['sessions_zscore']) > 3, 1, 0)
df['new_users_anomaly'] = np.where(np.abs(df['new_users_zscore']) > 3, 1, 0)
df['session_time_anomaly'] = np.where(np.abs(df['session_time_zscore']) > 3, 1, 0)


anomalies = df[(df['sessions_anomaly'] == 1) | (df['new_users_anomaly'] == 1) | (df['session_time_anomaly'] == 1)]
print(anomalies)
print(df)