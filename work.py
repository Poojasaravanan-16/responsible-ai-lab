python
raw_data = {
}
"username": "userl",
"password hash": "...",
"email": "user@example.com",
I
"location": "GPS COORDINATES",
"age": 25 
def minimize data (data):
minimized = {k: v for k, v in data.items() if k in ["username", "email", "age"]}
return minimized
minimized data minimize data (raw data)
print (minimized data)