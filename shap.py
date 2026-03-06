import shap
import xgboost
X, y = shap.datasets.boston()
model = xgboost.train({"learning_rate": 0.1}, xgboost.DMatrix(X, label=y), 10)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
shap.summary_plot(shap_values, X)
