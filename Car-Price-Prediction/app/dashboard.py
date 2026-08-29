from pathlib import Path
#Pathlib is a built-in Python library used to work with file and folder paths in an easy and platform-independent way.

import streamlit as st
import pandas as pd
import plotly.express as px
# Get the absolute path of the folder where the current Python file is located.
# Example: .../Car_Price_Prediction/pages
BASE_DIR = Path(__file__).resolve().parent# Move one folder up from the current file's folder (project root)
# and create the path to the "data" folder.
# Example: .../Car_Price_Prediction/data
DATA_DIR = BASE_DIR.parent / "data"

def dashboard_page():

    df = pd.read_csv(DATA_DIR / "car_data_preprocessed.csv")

    st.title("📊 Analytics Dashboard")

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Cars", len(df))
    c2.metric("Features", df.shape[1])
    c3.metric("Average Price", f"{df['Selling_Price'].mean():.2f} L")
    c4.metric("Maximum Price", f"{df['Selling_Price'].max():.2f} L")

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            df,
            x="Selling_Price",
            nbins=20,
            title="Selling Price Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.scatter(
            df,
            x="Present_Price",
            y="Selling_Price",
            color="Owner",
            title="Present Price vs Selling Price"
        )

        st.plotly_chart(fig, use_container_width=True)
        # Streamlit function used to display a Plotly graph on your web application.
        

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        fuel = pd.read_csv(DATA_DIR / "car data.csv")

        fig = px.pie(
            fuel,
            names="Fuel_Type",
            title="Fuel Type Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col4:

        fig = px.bar(
            fuel.sort_values("Selling_Price", ascending=False).head(10),
            x="Car_Name",
            y="Selling_Price",
            title="Top 10 Most Expensive Cars"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("Correlation Matrix")

    corr = df.corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Viridis"
    )

    st.plotly_chart(fig, use_container_width=True)
