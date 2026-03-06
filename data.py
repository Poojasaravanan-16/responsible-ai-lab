python
# Simulated database
database = {
"user1": {"name": "Alice", "data": "..." }, "user2": { "name": "Bob", "data": "..." }
}
def delete user data (user id):
if user id in database:
del database [user id]
print (f"User (user id) data deleted.")
else:
print ("User not found.")
# Usage
delete user data ("user1")