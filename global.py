from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
rf = RandomForestClassifier()
rf.fit(X, y)
importances = pd.Series(rf.feature_importances_, index=iris.feature_names)
importances.nlargest(4).plot(kind='barh')
plt.title("Global Feature Importance (Random Forest)")
plt.show()