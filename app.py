from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model & scaler
kmeans = pickle.load(open("kmeans_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    units = float(request.form["units"])
    revenue = float(request.form["revenue"])
    discount = float(request.form["discount"])
    ad_spend = float(request.form["ad_spend"])
    conversion = float(request.form["conversion"])

    data = np.array([[units, revenue, discount, ad_spend, conversion]])
    scaled_data = scaler.transform(data)

    cluster = kmeans.predict(scaled_data)[0]

    return render_template(
        "index.html",
        prediction=f"Product belongs to Cluster {cluster}"
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)