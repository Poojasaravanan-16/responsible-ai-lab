from faker import Faker
import pandas as pd
fake = Faker()
data = {
    'name': [fake.name() for _ in range(3)],
    'email': [fake.email() for _ in range(3)],
    'salary': [100000, 80000, 120000]
}
df = pd.DataFrame(data)
df['name'] = [fake.name() for _ in range(len(df))]
df['email'] = [fake.safe_email() for _ in range(len(df))]
print(df)