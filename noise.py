import hashlib

def anonymize_user_input(user_id, prompt):
    hashed_id = hashlib.sha256(user_id.encode()).hexdigest()
    return f"User {hashed_id} queried: [REDACTED]"

print(anonymize_user_input("user_123", "My bank account number is 1234"))
