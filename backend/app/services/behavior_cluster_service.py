import numpy as np
from sklearn.cluster import KMeans

# Sample behavioral training data
# [amount, device_change, location_change, frequency]

data = np.array([
    [200,0,0,1],
    [300,0,0,1],
    [1500,0,0,2],
    [5000,1,1,4],
    [7000,1,1,5],
    [9000,1,1,5],
    [400,0,1,2],
    [800,0,0,2]
])

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)


def predict_behavior_cluster(amount, device_change, location_change, frequency):

    sample = np.array([[amount, device_change, location_change, frequency]])

    cluster = kmeans.predict(sample)[0]

    cluster_map = {
        0: "Normal User",
        1: "Active User",
        2: "Suspicious Behaviour"
    }

    return {
        "cluster_id": int(cluster),
        "cluster_type": cluster_map.get(cluster, "Unknown")
    }