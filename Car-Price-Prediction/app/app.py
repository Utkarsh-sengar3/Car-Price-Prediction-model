
import streamlit as st 
#Python framework used to build web applications for machine learning and data science.


from prediction import prediction_page
from dashboard import dashboard_page
from model_info import model_page
from about import about_page


st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

st.sidebar.title("🚗 Car Price Prediction")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Prediction",
        "Dashboard",
        "Model Performance",
        "About"
    ]
)

if page == "Home":
    st.markdown("""
    <style>

    .hero{
        background:linear-gradient(135deg,#0F2027,#203A43,#2C5364);
        padding:40px;
        border-radius:20px;
        color:white;
        box-shadow:0px 10px 30px rgba(0,0,0,0.4);
    }

    .hero h1{
        font-size:52px;
        margin-bottom:10px;
    }

    .hero p{
        font-size:20px;
        color:#DDDDDD;
    }

    .card{
        background:#1E1E1E;
        border-radius:18px;
        padding:25px;
        text-align:center;
        box-shadow:0px 8px 18px rgba(0,0,0,.35);
        transition:.3s;
        height:170px;
    }

    .card:hover{
        transform:translateY(-6px);
        box-shadow:0px 12px 28px rgba(0,0,0,.5);
    }

    .number{
        font-size:42px;
        font-weight:bold;
        color:white;
    }

    .title{
        color:#A0A0A0;
        font-size:18px;
    }

    .feature{
        background:#252525;
        border-radius:15px;
        padding:20px;
        text-align:center;
        height:170px;
    }

    .feature h3{
        color:white;
    }

    .feature p{
        color:#CFCFCF;
    }

    .workflow{
        background:#1E1E1E;
        border-radius:15px;
        padding:25px;
        color:white;
    }

    .footer{
        text-align:center;
        color:#BBBBBB;
        font-size:17px;
        margin-top:40px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">

    <h1>🚗 Car Price Prediction</h1>

    <p>
    Predict the selling price of used cars using Machine Learning.
    This project uses a Random Forest Regression model to estimate
    the market value of a used car based on its specifications.
    </p>

    </div>
    """, unsafe_allow_html=True) 
    #Streamlit interprets the HTML correctly and renders it as a webpage.
    

    st.write("")
    st.write("")

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
        <div class="title">🚘 Cars</div>
        <br>
        <div class="number">299</div>
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <div class="title">⚡ Features</div>
        <br>
        <div class="number">8</div>
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <div class="title">🤖 Model</div>
        <br>
        <div style="font-size:26px;font-weight:bold;color:white;">
        Random Forest
        </div>
        </div>
        """,unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
        <div class="title">🎯 Accuracy</div>
        <br>
        <div class="number">94.8%</div>
        </div>
        """,unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.subheader("✨ Project Features")

    f1,f2,f3=st.columns(3)

    with f1:
        st.markdown("""
        <div class="feature">
        <h3>⚡ Fast Prediction</h3>
        <p>
        Predict used car selling prices instantly with one click.
        </p>
        </div>
        """,unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature">
        <h3>📊 Analytics Dashboard</h3>
        <p>
        Interactive Power BI dashboard for visual analysis.
        </p>
        </div>
        """,unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="feature">
        <h3>🤖 Machine Learning</h3>
        <p>
        Built using Random Forest Regression with high accuracy.
        </p>
        </div>
        """,unsafe_allow_html=True)

    st.write("")
    st.write("")

    left,right=st.columns([2,1])

    with left:

        st.subheader("⚙️ Project Workflow")

        st.markdown("""
        <div class="workflow">

        📂 Used Car Dataset

        ⬇

        🧹 Data Cleaning

        ⬇

        ⚙ Feature Engineering

        ⬇

        🌲 Random Forest Training

        ⬇

        🚗 Selling Price Prediction

        </div>
        """,unsafe_allow_html=True)

    with right:

        st.subheader("📌 Project Details")

        st.info("""
**Algorithm**

Random Forest Regressor

**Programming**

Python

**Framework**

Streamlit

**Visualization**

Power BI

**Dataset**

Used Car Dataset
""")

    st.write("")
    st.write("")

    st.markdown("""
    <div class="footer">

    ---
    Developed by

    <b>Utkarsh Sengar</b> & <b>Pritish Kumar</b>

    AI & ML Engineering

    Lovely Professional University

    </div>
    """,unsafe_allow_html=True)
#     st.title("🚗 Car Price Prediction")

#     st.write(
#         """
# Welcome to the Car Price Prediction System.

# This application predicts the selling price of a used car using Machine Learning.
# """
#     )

#     c1, c2, c3 = st.columns(3)

#     c1.metric("Cars", "299")

#     c2.metric("Features", "8")

#     c3.metric("Best Model", "Random Forest")


elif page == "Prediction":

    prediction_page()

elif page == "Dashboard":

     dashboard_page()

elif page == "Model Performance":
    model_page()

elif page == "About":

    about_page()