import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .main{
        background-color:#f6fbf7;
    }

    h1,h2,h3{
        color:#1b5e20;
    }

    .stButton>button{
        width:100%;
        background:#2e7d32;
        color:white;
        border-radius:10px;
        border:none;
        height:50px;
        font-size:17px;
        font-weight:bold;
    }

    .stButton>button:hover{
        background:#1b5e20;
        color:white;
    }

    .metric-card{
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.08);
        text-align:center;
        margin-bottom:15px;
    }

    .metric-title{
        font-size:15px;
        color:#666;
    }

    .metric-value{
        font-size:24px;
        color:#2e7d32;
        font-weight:bold;
    }

    .section-card{
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.08);
        margin-bottom:15px;
    }

    .header-box{
        background:linear-gradient(90deg,#2e7d32,#66bb6a);
        color:white;
        padding:20px;
        border-radius:15px;
        margin-bottom:20px;
    }

    </style>
    """, unsafe_allow_html=True)