import streamlit as st

def about_page():

    st.title("📖 About Project")

    st.write("""
# 🚗 Car Price Prediction System

This project predicts the selling price of a used car using Machine Learning.

The model has been trained using historical car data and can estimate the resale value based on several important features.
""")

    st.markdown("---")

    st.header("🎯 Objective")

    st.write("""
The objective of this project is to build an accurate machine learning model
that predicts used car prices based on:

- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Number of Owners
- Car Age
""")

    st.markdown("---")

    st.header("⚙️ Project Workflow")

    st.write("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis

4. Feature Engineering

5. Model Training

6. Hyperparameter Tuning

7. Model Evaluation

8. Streamlit Deployment
""")

    st.markdown("---")

    st.header("🧠 Machine Learning")

    st.write("""
Models Used

• Linear Regression

• Decision Tree Regressor

• Random Forest Regressor

Best Model

🏆 Random Forest Regressor
""")

    st.markdown("---")

    st.header("💻 Technologies")

    st.write("""
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Streamlit
""")

    st.markdown("---")

    st.header("👨‍💻 Developers")

    st.success("""
Utkarsh Sengar & Pritish kumar
               
AI & ML Engineering

Lovely Professional University
""")