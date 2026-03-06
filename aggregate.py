bins = [0, 18, 35, 50, 100]
labels = ['<18', '18-35', '36-50', '50+']
df_minimized['AgeGroup'] = pd.cut(df_minimized['Age'], bins=bins, labels=labels)
df_minimized = df_minimized.drop(columns=['Age'])
print("\nDataFrame with Aggregated Age Group:")
print(df_minimized)