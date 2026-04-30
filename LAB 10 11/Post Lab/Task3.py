import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv("marketing_campaign.csv")

X = data[["Income", "MntWines"]]
X["Income"] = X["Income"].fillna(X["Income"].mean())
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
inertia = []
for k in range(2, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_scaled)
    inertia.append(model.inertia_)

plt.plot(range(2, 11), inertia, marker='o')
plt.xlabel("K")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()


kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)

data["Cluster"] = labels

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels)
plt.xlabel("Income")
plt.ylabel("Wine Spending")
plt.title("Customer Segments")
plt.show()

print(data[["Income", "MntWines", "Cluster"]].head())
