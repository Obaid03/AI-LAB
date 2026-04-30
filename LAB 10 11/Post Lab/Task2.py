import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = pd.read_csv("train.csv")
num_cols = data.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    data[col] = data[col].fillna(data[col].median())
cat_cols = data.select_dtypes(include=['object']).columns
for col in cat_cols:
    data[col] = data[col].fillna(data[col].mode()[0])
data = pd.get_dummies(data, drop_first=True)

y = data["SalePrice"]
X = data.drop("SalePrice", axis=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)
lr = LinearRegression()
dt = DecisionTreeRegressor(random_state=42)
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)
pred_lr = lr.predict(X_test)
pred_dt = dt.predict(X_test)

def evaluate(name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"\n{name}")
    print("MAE :", mae)
    print("RMSE:", rmse)

evaluate("Linear Regression", y_test, pred_lr)
evaluate("Decision Tree", y_test, pred_dt)
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted_LR": pred_lr,
    "Predicted_DT": pred_dt
})

print("\nSample Predictions:")
print(results.head(10))
