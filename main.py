import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st
import yfinance as yf
import pandas as pd


from time import sleep
from tracemalloc import start
from matplotlib import ticker
from 1_🫤_data1 import data1_function

st.set_page_config(
    page_icon="📊",
    page_title="GPV",
    layout="wide"
)

st.sidebar.title('this is sidebar')
selected_page = st.sidebar.selectbox("Select a page", ["Home", "data1"])

if selected_page == "Home":
    home()
elif selected_page == "data1":
    data1_function()


def home():
    st.title('GPV')
    st.write('The fluctuation of oil prices from April 15, 2008, to November 29, 2023.')



    # CSV 파일 불러오기
    data = pd.read_csv("neural.csv")

    # 최대, 최소 날짜 설정
    max_date = pd.to_datetime('2023-11-29').date()
    min_date = pd.to_datetime('2008-04-15').date()
    

    start = st.date_input('Start Date', value=pd.to_datetime('2008-04-15'), min_value = min_date, max_value = max_date)
    end = st.date_input('End Date',value=pd.to_datetime('2023-11-29'), min_value = min_date, max_value = max_date)


    if 'ds' in data.columns and 'y' in data.columns:
        df = data[['ds', 'y']].copy()
        df['ds'] = pd.to_datetime(df['ds'])

        st.line_chart(df.set_index('ds').loc[start:end])
    else:
        st.warning("CSV 파일은 'ds'와 'y' 열을 포함해야 합니다.")
        None
    



