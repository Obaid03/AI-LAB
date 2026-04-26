import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    'student_id': [1,2,3,4,5,6,7,8,9,10],
    'GPA': [2.5,3.2,3.8,2.0,3.5,3.0,1.8,3.9,2.7,3.3],
    'study_hours': [10,15,20,5,18,14,4,22,12,16],
    'attendance_rate': [70,85,95,60,90,80,55,98,75,88]
}
df = pd.DataFrame(data)
X = df[['GPA','study_hours','attendance_rate']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
inertia = []
k_range = range(2,7)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=1)
    km.fit(X_scaled)
    inertia.append(km.inertia_)
plt.figure()
plt.plot(k_range, inertia, marker='o')
plt.xlabel("K")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()
optimal_k = 3
model = KMeans(n_clusters=optimal_k, random_state=1)
df['cluster'] = model.fit_predict(X_scaled)
plt.figure()
plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'])
plt.xlabel("Study Hours")
plt.ylabel("GPA")
plt.title("Student Clusters")
plt.show()
print(df[['student_id','cluster']])
