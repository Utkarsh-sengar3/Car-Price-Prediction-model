import streamlit as st
import pandas as pd
import joblib

st.write("prediction.py imported successfully")

from pathlib import Path

BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / "best_car_price_model.pkl")
features = joblib.load(BASE_DIR / "features.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")
# import streamlit as st
# import pandas as pd
# import joblib

# # -----------------------
# # Load Model
# # -----------------------

# model = joblib.load("best_car_price_model.pkl")
# features = joblib.load("features.pkl")
# scaler = joblib.load("scaler.pkl")


def prediction_page():
    st.success("✅ Prediction Page Loaded Successfully")
    

    st.title("🚗 Predict Selling Price")

    st.write("Fill in the vehicle details below.")

    col1, col2 = st.columns(2)

    with col1:

        present_price = st.number_input(
            "Present Price (Lakhs)",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.1
        )

        kms_driven = st.number_input(
            "Kilometers Driven",
            min_value=0,
            value=25000,
            step=500
        )

        owner = st.selectbox(
            "Previous Owners",
            [0,1,2,3]
        )

        car_age = st.slider(
            "Car Age",
            0,
            25,
            5
        )

    with col2:

        fuel = st.selectbox(
            "Fuel Type",
            [
                "Petrol",
                "Diesel"
            ]
        )

        seller = st.selectbox(
            "Seller Type",
            [
                "Dealer",
                "Individual"
            ]
        )

        transmission = st.selectbox(
            "Transmission",
            [
                "Manual",
                "Automatic"
            ]
        )

    if st.button("Predict Price"):

        input_data = {
            "Present_Price": present_price,
            "Kms_Driven": kms_driven,
            "Owner": owner,
            "Car_Age": car_age,
            "Fuel_Type_Diesel": 1 if fuel=="Diesel" else 0,
            "Fuel_Type_Petrol": 1 if fuel=="Petrol" else 0,
            "Seller_Type_Individual": 1 if seller=="Individual" else 0,
            "Transmission_Manual": 1 if transmission=="Manual" else 0,
        }

        input_df = pd.DataFrame([input_data])

        # Ensure feature order matches training
        input_df = input_df.reindex(columns=features, fill_value=0)

        prediction = model.predict(input_df)[0]

        st.success(
            f"Estimated Selling Price : ₹ {prediction:.2f} Lakhs"
        )

        st.markdown("---")

        st.subheader("Input Summary")

        st.dataframe(input_df)

        csv = pd.DataFrame({
            "Predicted Price":[prediction]
        }).to_csv(index=False)

        st.download_button(
            "📥 Download Prediction",
            csv,
            "prediction.csv",
            "text/csv"
        )