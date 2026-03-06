from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
X, y = iris.data, iris.target
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X, y)
plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()