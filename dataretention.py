from datetime import datetime, timedelta
df_retention = pd.DataFrame({
    'UserID': [1, 2],
    'Data': ['A', 'B'],
    'CollectionDate': [datetime.now(), datetime.now() - timedelta(days=366)]
})
retention_period_days = 365
cutoff_date = datetime.now() - timedelta(days=retention_period_days)
df_current = df_retention[df_retention['CollectionDate'] >= cutoff_date]
print("\nData after applying retention policy:")
print(df_current)
