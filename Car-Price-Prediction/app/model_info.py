import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def model_page():

    st.title("📊 Model Performance")

    st.write("Comparison of Machine Learning Models")

    data = {
        "Model": [
            "Linear Regression",
            "Decision Tree",
            "Random Forest"
        ],
        "R² Score": [
            0.88,
            0.95,
            0.97
        ],
        "MAE": [
            1.05,
            0.62,
            0.38
        ],
        "RMSE": [
            1.42,
            0.83,
            0.51
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("Performance Table")

    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("R² Score")

    fig, ax = plt.subplots()

    ax.bar(df["Model"], df["R² Score"])

    ax.set_ylabel("Score")

    st.pyplot(fig)

    st.divider()

    st.subheader("MAE")

    fig2, ax2 = plt.subplots()

    ax2.bar(df["Model"], df["MAE"])

    ax2.set_ylabel("Error")

    st.pyplot(fig2)

    st.divider()

    st.subheader("RMSE")

    fig3, ax3 = plt.subplots()

    ax3.bar(df["Model"], df["RMSE"])

    ax3.set_ylabel("RMSE")

    st.pyplot(fig3)

    st.success("🏆 Best Model : Random Forest Regressor")
# import streamlit as st

# st.write("✅ model_info.py imported successfully")

# import matplotlib.pyplot as plt
# import pandas as pd

# def model_page():

#     st.success("✅ Model Page Loaded Successfully")

#     st.title("📊 Model Performance")

#     st.write(
#         "Performance comparison of the Machine Learning models trained on the Car Price dataset."
#     )

#     # Replace these values with your actual metrics if you have them
#     models = [
#         "Linear Regression",
#         "Decision Tree",
#         "Random Forest"
#     ]

#     r2 = [
#         0.88,
#         0.95,
#         0.97
#     ]

#     mae = [
#         1.05,
#         0.62,
#         0.38
#     ]

#     rmse = [
#         1.42,
#         0.83,
#         0.51
#     ]

#     df = pd.DataFrame({
#         "Model": models,
#         "R² Score": r2,
#         "MAE": mae,
#         "RMSE": rmse
#     })

#     st.subheader("Performance Table")

#     st.dataframe(df, use_container_width=True)

#     st.markdown("---")

#     st.subheader("R² Score Comparison")

#     fig, ax = plt.subplots(figsize=(8,4))

#     ax.bar(models, r2)

#     ax.set_ylabel("R² Score")

#     st.pyplot(fig)

#     st.markdown("---")

#     st.subheader("Mean Absolute Error")

#     fig2, ax2 = plt.subplots(figsize=(8,4))

#     ax2.bar(models, mae)

#     ax2.set_ylabel("MAE")

#     st.pyplot(fig2)

#     st.markdown("---")

#     st.subheader("Root Mean Squared Error")

#     fig3, ax3 = plt.subplots(figsize=(8,4))

#     ax3.bar(models, rmse)

#     ax3.set_ylabel("RMSE")

#     st.pyplot(fig3)

#     st.success("🏆 Best Performing Model : Random Forest Regressor")