import pandas as pd
df = pd.read_csv('user_data.csv')
df_anonymized = df.drop(columns=['name''social_security_no'])
df_anonymized.to_csv('safe_data.csv', index=False)
