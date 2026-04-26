import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}
df = pd.DataFrame(data)
encoded = pd.get_dummies(df['vehicle_type'])
X = pd.concat([df.drop(['vehicle_serial_no','vehicle_type'], axis=1), encoded], axis=1)
k1 = KMeans(n_clusters=3, random_state=2)
df['cluster_no_scaling'] = k1.fit_predict(X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
k2 = KMeans(n_clusters=3, random_state=2)
df['cluster_with_scaling'] = k2.fit_predict(X_scaled)
print("Without Scaling:\n", df[['mileage','fuel_efficiency','maintenance_cost','vehicle_type','cluster_no_scaling']])
print("With Scaling:\n", df[['mileage','fuel_efficiency','maintenance_cost','vehicle_type','cluster_with_scaling']])
print("Without scaling mileage dominates, after scaling clustering is more balanced across all features.")
