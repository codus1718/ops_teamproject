import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st
import yfinance as yf
import pandas as pd


from time import sleep
from tracemalloc import start
from matplotlib import ticker

st.set_page_config(
    page_icon="📊",
    page_title="GPVP",
    layout="wide"
)

st.title('GPVP')
st.write('The fluctuation of oil prices from April 15, 2008, to November 29, 2023.')

columns = st.columns((1, 1, 2))
columns[0].metric("A")
columns[0].metric("B")



# CSV 파일 불러오기
data = pd.read_csv("neural.csv")

# 최대, 최소 날짜 설정
max_date = pd.to_datetime('2023-11-29').date()
min_date = pd.to_datetime('2008-04-15').date()


start = st.date_input('Start', value=pd.to_datetime('2008-04-15'), max_value = max_date)
end = st.date_input('End',value=pd.to_datetime('2023-11-29'), min_value = min_date, max_value = max_date)


if 'ds' in data.columns and 'y' in data.columns:
    df = data[['ds', 'y']].copy()
    df['ds'] = pd.to_datetime(df['ds'])

    visualization_chart = st.line_chart(df.set_index('ds').loc[start:end])
else:
    st.warning("CSV 파일은 'ds'와 'y' 열을 포함해야 합니다.")
    visualization_chart = None
    
columns[1].metric(visualization_chart)


