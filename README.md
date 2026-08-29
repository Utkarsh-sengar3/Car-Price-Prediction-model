# 🚗 Car Price Prediction

<p align="center">
  <b>Machine Learning Web Application for Predicting Used Car Prices</b>
</p>

<p align="center">
  Predict the estimated price of a used car using Machine Learning and an easy-to-use Streamlit interface.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 📌 About The Project

**Car Price Prediction** is a Machine Learning-based web application designed to estimate the selling price of a used car based on various features such as car specifications, usage, and other relevant attributes.

The project uses a **Random Forest Regression** model to learn patterns from historical car-price data and provide price predictions through an interactive **Streamlit** web interface.

The goal of this project is to demonstrate the complete Machine Learning workflow:

> **Data → Preprocessing → Model Training → Prediction → Web Application**

---

## ✨ Features

- 🚘 Predict the estimated price of a used car
- 🤖 Random Forest Regression Machine Learning model
- 📊 Data preprocessing and feature handling
- 🌐 Interactive Streamlit web interface
- ⚡ Fast predictions
- 🎨 Simple and user-friendly interface
- 🧠 End-to-end Machine Learning implementation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 **Python** | Core programming language |
| 🌲 **Random Forest Regression** | Price prediction model |
| 🧮 **Scikit-learn** | Machine Learning |
| 📊 **Pandas** | Data processing |
| 🔢 **NumPy** | Numerical computation |
| 🎨 **Streamlit** | Web application |
| 📈 **Matplotlib / Seaborn** | Data visualization |

---

## 🧠 Machine Learning Model

The project uses **Random Forest Regression** for predicting car prices.

Random Forest is an ensemble learning algorithm that combines multiple decision trees to produce a more robust and accurate prediction.

### 🔄 Model Workflow

```text
             ┌─────────────────┐
             │   Car Dataset   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Data Cleaning   │
             │ & Preprocessing │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Feature         │
             │ Engineering     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Random Forest   │
             │   Regression    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Price Prediction│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Streamlit Web   │
             │      App        │
             └─────────────────┘
