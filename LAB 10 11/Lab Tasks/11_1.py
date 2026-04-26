import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'customer_id': [1,2,3,4,5,6,7,8],
    'age': [22,35,45,23,40,30,50,28],
    'income': [30000,60000,80000,25000,75000,50000,90000,45000],
    'spending_score': [40,60,80,30,70,55,85,50],
    'visits': [5,12,18,4,15,10,20,8]
}
df = pd.DataFrame(data)
X = df.drop('customer_id', axis=1)
k1 = KMeans(n_clusters=2, random_state=0)
df['cluster_no_scaling'] = k1.fit_predict(X)
scaler = StandardScaler()
scaled_part = scaler.fit_transform(X.drop('age', axis=1))
scaled_df = pd.concat([pd.DataFrame(X['age']).reset_index(drop=True), pd.DataFrame(scaled_part)], axis=1)
k2 = KMeans(n_clusters=2, random_state=0)
df['cluster_with_scaling'] = k2.fit_predict(scaled_df)
print("Without Scaling:\n", df[['age','income','spending_score','visits','cluster_no_scaling']])
print("With Scaling:\n", df[['age','income','spending_score','visits','cluster_with_scaling']])
print("Clusters without scaling are mostly influenced by income values.")
