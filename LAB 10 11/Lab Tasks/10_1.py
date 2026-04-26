import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

house_data = {
    'area': [1100, 1600, 1900, 2500, 3100, 1400],
    'beds': [2, 3, 3, 4, 5, 2],
    'baths': [1, 2, 2, 3, 4, 1],
    'house_age': [12, 6, 9, 3, 2, 15],
    'zone': ['A', 'B', 'A', 'B', 'C', 'A'],
    'cost': [210000, 310000, 330000, 420000, 520000, 250000]
}

df = pd.DataFrame(house_data)
df.fillna(method='ffill', inplace=True)
df = pd.get_dummies(df, columns=['zone'], drop_first=True)
features = df.drop('cost', axis=1)
target = df['cost']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
predictions = lr_model.predict(X_test)
print("------ Model Evaluation ------")
print("Predicted values:", predictions)
print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))
sample_house = [[2100, 3, 2, 5, 1, 0]]
estimated_price = lr_model.predict(sample_house)
print("Estimated Price:", estimated_price[0])
