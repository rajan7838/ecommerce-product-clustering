# E-Commerce Product Clustering (K-Means + Flask Deployment)

## Project Objective
Cluster products based on purchase behavior and marketing performance to identify high-performing, average, and low-performing products. Deployed the trained model using Flask for real-time predictions.
“I built an end-to-end unsupervised machine learning project using K-Means clustering on an e-commerce dataset.
The goal was to understand product purchase behavior and segment products based on sales, revenue, discounts, advertising spend, and conversion rate.
I first aggregated data at the product level and applied feature scaling using StandardScaler.
To choose the optimal number of clusters, I used the Elbow Method.
After training the final K-Means model, I interpreted each cluster in business terms such as high-performing, medium-performing, and low-performing products.
Finally, I deployed the trained model using Flask, where users can input product metrics and get the predicted cluster in real time.”

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
