import pandas as pd
from sklearn.tree import    DecisionTreeClassifier  
from sklearn.metrics import accuracy_score
from fairlearn.metrics import MetricFrame,demographic_parity_difference
from fairlearn.datasets import make_adult_df

df = make_adult_df()
X = df.drop(columns=['income',axis=1])
y = df['income']
sensitive_feature['age_group']= sensitive_feature['age']