# E-Commerce Product Clustering (K-Means + Flask Deployment)

## Project Objective
Cluster products based on purchase behavior and marketing performance to identify high-performing, average, and low-performing products. Deployed the trained model using Flask for real-time predictions.

## Features Used
- Units_Sold
- Revenue
- Discount_Applied
- Ad_Spend
- Conversion_Rate

## Steps
1. **Data Aggregation:** Aggregated per product.
2. **Scaling:** StandardScaler applied.
3. **Elbow Method:** To find optimal K.
4. **Model Training:** KMeans clustering with K=3.
5. **Model Saving:** Saved `kmeans_model.pkl` & `scaler.pkl`.
6. **Deployment:** Flask app with real-time prediction.
