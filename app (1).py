from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)
app.secret_key = "secret_key"  # required for session

# Load model and scalers
model = joblib.load('model.pkl')
sc = joblib.load('standscaler.pkl')
ms = joblib.load('minmaxscaler.pkl')


@app.route('/')
def index():
    result = session.pop("result", None)  # remove after showing
    return render_template("index.html", result=result)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])

        feature_list = [N, P, K, temp, humidity, ph, rainfall]

        columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        single_pred = pd.DataFrame([feature_list], columns=columns)

        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)

        prediction = model.predict(final_features)

        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop = crop_dict.get(prediction[0], "Unknown Crop")
        result = f"🌱 Recommended Crop: {crop}"

    except Exception as e:
        result = f"Error: {str(e)}"

    # Store result and redirect (PRG pattern)
    session["result"] = result
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))