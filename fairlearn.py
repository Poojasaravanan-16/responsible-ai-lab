from fairlearn.metrics import MetricFrame, selection_rate
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mf = MetricFrame(metrics=selection_rate, y_true=y_test, y_pred=y_pred, sensitive_features=X_test['gender'])
print(mf.by_group)