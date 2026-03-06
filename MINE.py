from lime.lime_tabular import LimeTabularExplainer
lime_exp = LimeTabularExplainer(
    X_train.values,
    feature_names=list(X.columns),
    class_names=["benign", "malignant"],
    mode="classification"
)
i = 0
exp = lime_exp.explain_instance(X_test.iloc[i].values, clf.predict_proba)
exp.show_in_notebook()
