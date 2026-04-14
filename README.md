# 🌱 Crop Recommendation System

A Machine Learning-powered web application that recommends the most suitable crop to grow based on soil nutrients and environmental conditions.

---

## 🚀 Live Demo

👉 https://crop-recommendation-system-fesu.onrender.com

⚠️ *Note: The app may take 30–60 seconds to load initially due to free hosting (cold start).*

---

## 🧠 Project Overview

This project uses a trained Machine Learning model to analyze key agricultural parameters such as Nitrogen, Phosphorus, Potassium levels, temperature, humidity, pH, and rainfall to suggest the best crop for cultivation.

It is designed to help farmers and agricultural enthusiasts make data-driven decisions for better yield.

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn
* **Frontend:** HTML, CSS, Bootstrap
* **Data Processing:** Pandas, NumPy
* **Model Deployment:** Render

---

## 📊 Features

✅ Predicts the best crop based on input conditions
✅ Clean and user-friendly interface
✅ Fast and efficient ML predictions
✅ End-to-end ML pipeline (preprocessing + model)
✅ Deployed and accessible online

---

## 📥 Input Parameters

The model takes the following inputs:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature (°C)
* Humidity (%)
* pH value
* Rainfall (mm)

---

## 📤 Output

* 🌾 Recommended crop for cultivation

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/inetsudhanshu-cse/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

### 2️⃣ Create virtual environment

```bash
python -m venv crop_env
crop_env\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
Crop-Recommendation-System/
│
├── app.py
├── model.pkl
├── standscaler.pkl
├── minmaxscaler.pkl
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   └── img.jpg
│
└── dataset/
    └── Crop_recommendation.csv
```

---

## 🚀 Future Improvements

* 🌐 Add React frontend
* 📊 Show prediction confidence
* 🌾 Display crop-specific images dynamically
* 📱 Make UI fully responsive
* ☁️ Use cloud storage for models

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 👨‍💻 Author

**Sudhanshu Kumar**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
