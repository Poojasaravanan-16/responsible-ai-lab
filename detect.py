import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = {
    'Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Gender':     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'Hired':      [0, 1, 0, 1, 0, 1, 1, 1, 0, 1]  
}
df = pd.DataFrame(data)
X = df[['Experience', 'Gender']]
y = df['Hired']
model = LogisticRegression().fit(X, y)
df['Prediction'] = model.predict(X)
female_hired_rate = df[df['Gender'] == 0]['Prediction'].mean()
male_hired_rate = df[df['Gender'] == 1]['Prediction'].mean()

print(f"Female Hiring Rate: {female_hired_rate:.2f}")
print(f"Male Hiring Rate: {male_hired_rate:.2f}")
fairness_metric = male_hired_rate - female_hired_rate
print(f"\nBias Metric (Selection Rate Difference): {fairness_metric:.2f}")

if fairness_metric > 0.1:
    print("WARNING: Model shows significant bias against females.")