import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv("creditcard.csv")
fraud = data[data["Class"] == 1]
normal = data[data["Class"] == 0]
normal_sample = normal.sample(len(fraud), random_state=42)
balanced_data = pd.concat([fraud, normal_sample])
balanced_data = balanced_data.sample(frac=1, random_state=42)
X = balanced_data.drop("Class", axis=1)
y = balanced_data["Class"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

lr = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier(random_state=42)
lr.fit(X_train, y_train)
rf.fit(X_train, y_train)
pred_lr = lr.predict(X_test)
pred_rf = rf.predict(X_test)

def print_results(name, y_true, y_pred):
    print(f"\n{name}")
    print("Accuracy :", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall   :", recall_score(y_true, y_pred))
    print("F1 Score :", f1_score(y_true, y_pred))

print_results("Logistic Regression", y_test, pred_lr)
print_results("Random Forest", y_test, pred_rf)
