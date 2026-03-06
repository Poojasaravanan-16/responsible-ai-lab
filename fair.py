import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from fairlearn.metrics import MetricFrame, demographic_parity_difference
from fairlearn.datasets import make_adult_df
df = make_adult_df()
X = df.drop("income", axis=1)
y = df["income"]
sensitive_features = df[['age']]
sensitive_features['age_group'] = sensitive_features['age'].apply(lambda x: 'old' if x >= 40 else 'young')
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
y_pred = model.predict(X)
mf = MetricFrame(metrics={"accuracy": accuracy_score,
                          "demographic_parity_difference": demographic_parity_difference},
                 y_true=y,
                 y_pred=y_pred,
                 sensitive_features=sensitive_features['age_group'])

print("Fairness Assessment Results:")
print(mf.overall)
print("\nMetrics by group:")
print(mf.by_group)