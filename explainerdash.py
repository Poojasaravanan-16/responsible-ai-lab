from explainerdashboard import ClassifierExplainer, ExplainerDashboard
explainer = ClassifierExplainer(clf, X_test, y_test)
ExplainerDashboard(explainer).run()