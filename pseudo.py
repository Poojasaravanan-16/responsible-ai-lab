import hashlib
def hash_id(user_id):
    return hashlib.sha256(str(user_id).encode()).hexdigest()[:10]
df_pseudonymized = df_minimized.copy()
df_pseudonymized['UserID'] = df_pseudonymized['UserID'].apply(hash_id)
print("\nDataFrame with Pseudonymized User IDs:")
print(df_pseudonymized)