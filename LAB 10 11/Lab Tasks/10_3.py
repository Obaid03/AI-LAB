import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report

records = {
    'total_spent': [600, 1800, 2200, 350, 2700, 800, 1600, 450],
    'cust_age': [24, 40, 47, 21, 52, 29, 38, 23],
    'store_visits': [6, 18, 20, 4, 22, 7, 15, 5],
    'buy_freq': [2, 6, 7, 1, 8, 3, 5, 2],
    'class': [0, 1, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(records)
df = df.fillna(df.median(numeric_only=True))
for c in ['total_spent', 'cust_age', 'store_visits', 'buy_freq']:
    low = df[c].quantile(0.05)
    high = df[c].quantile(0.95)
    df[c] = np.clip(df[c], low, high)
X = df[['total_spent', 'cust_age', 'store_visits', 'buy_freq']]
y = df['class']
sc = MinMaxScaler()
X_scaled = sc.fit_transform(X)
X_tr, X_te, y_tr, y_te = train_test_split(X_scaled, y, test_size=0.25, random_state=1)
clf = LogisticRegression()
clf.fit(X_tr, y_tr)
preds = clf.predict(X_te)
print("Accuracy:", accuracy_score(y_te, preds))
print(classification_report(y_te, preds))
dt = DecisionTreeClassifier(max_depth=2)
dt.fit(X_tr, y_tr)
print("Rules:")
print(export_text(dt, feature_names=['total_spent','cust_age','store_visits','buy_freq']))
