# 📊 K-Means Clustering Visualizer

An interactive web-based tool to understand and visualize the K-Means Clustering Algorithm.

🔗 Live Demo: https://k-means-clustering.netlify.app/

---

## 🚀 Features

- Interactive clustering visualization  
- Dynamic centroid updates  
- Elbow Method implementation  
- Inertia (WCSS) analysis  
- Cluster visualization  
- Data scaling support  

---

## ✅ Validation Criteria

### ▸ Can you explain how centroids are updated?
Yes. Centroids are updated by computing the **mean of all data points assigned to each cluster**.  
This process is repeated iteratively until the centroids no longer change significantly (convergence).

---

### ▸ Did you generate an Elbow plot successfully?
Yes. The application generates an **Elbow Plot** showing:
- X-axis → Number of clusters (K)  
- Y-axis → Inertia (WCSS)  

This helps identify the optimal value of K.

---

### ▸ Can you interpret inertia values?
Yes. Inertia represents the **sum of squared distances between data points and their cluster centroids**.

- Lower inertia → Better clustering (tight clusters)  
- Higher inertia → Poor clustering  

---

### ▸ Is your data scaled before clustering?
Yes. Data scaling is performed before clustering to ensure:
- Equal importance of all features  
- Accurate distance calculations  

---

### ▸ Have you visualized the final clusters and centroids?
Yes. The application clearly visualizes:
- Clustered data points (different colors)  
- Centroids (highlighted markers)  

---

## 🛠️ Technologies Used

- HTML, CSS, JavaScript  
- K-Means Algorithm  

---

## ▶️ How to Use

1. Open the website  
2. Select K value  
3. Run clustering  
4. Observe clusters and elbow plot  

---

## 👨‍💻 Author

Bhavish Kumar
