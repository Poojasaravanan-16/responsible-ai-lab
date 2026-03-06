import pandas as pd
import numpy as np
from sklearn.model selection import train test split
from sklearn.preprocessing import StandardScaler
from sklearn.linear model import LogisticRegression
from sklearn.metrics import accuracy score
from fairlearn.metrics import MetricFrame, selection rate difference
from fairlearn.preprocessing import CorrelationRemover
from diffprivlib.models import LogisticRegression as DPLoReg
import shap
np.random.seed(42)
n samples = 1000
gender = np.random.binomial (1, 0.5, n samples)
income = np.random.normal (50000, 15000, n samples)
income = income + (gender* 10000)
loan approved = (income + np.random.normal(0, 10000, n samples) > 55000).astype (int)
data = pd. DataFrame({'gender': gender, 'income': income, 'loan approved': loan approved})
X = data [['gender', 'income']]
y = data['loan approved']
sensitive feature = data['gender'] 
train, X test, y train, y test, s train, s test = train test split(
X, y, sensitive feature, test size=0.3, random state=42
)
scaler StandardScaler ()
train scaled = scaler.fit transform (X train)
test scaled = scaler.transform (X test)
Ir = LogisticRegression (solver='liblinear')
lr.fit(X train scaled, y train)
preds=lr.predict(X_test_scaled)
print("----Initial Model (before fairness & privacy)----")
print(f"Accuracy: {accuracy_score(y_test, preds):.2f}")
sr_diff = selection_rate_difference(y_test, preds, sensitive_features=s_test)
print(f"Selection Rate Difference: {sr_diff:.2f}")
cr=correlationRemover(sensitive_feature_ids=['gender'])
x_train_fair=cr.fit_transform(X_train)
x_test_fair=cr.transform(X_test)
dp lr.DPLoReg (epsilon=1.0, data norm=10)
dp lr.fit(X train fair, y train)
dp preds dp lr.predict (X test fair)
print("\n--- Model After Fairness Mitigation & Differential Privacy ---")
print (f"DP Accuracy: {accuracy score (y test, dp preds):.2f}")
dp sr diff = selection rate difference (y test, dp preds, sensitive features=s test)
print (f"New Selection Rate Difference: {dp_sr_diff:.2f}")
print("\n-- Explainability (SHAP values) ---")
explainer = shap. LinearExplainer (dp lr, X train fair)
shap values = explainer.shap values (X test fair)
shap.summary plot (shap values, X test fair, feature names=['gender', 'income'], plot type="bar")
X test corrupted = X test fair.copy()
X test corrupted (:, 1) = X test corrupted[:, 1] + np.random.normal(0, 5,
X test corrupted.shape[0])
robust preds = dp lr.predict (X test corrupted)
print("\n--- Robustness Test ---")
print (f"Accuracy with corrupted data: {accuracy score (y test, robust preds):.2f}")
print("The DP model should show similar performance despite noise.")