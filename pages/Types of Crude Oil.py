import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_icon="📊",
    page_title="Types of Crude Oil",
    layout="wide"
)


st.title('Combined Price Trends of WTI, Brent, Dubai, and Gasoline')


# 두 개의 CSV 파일을 읽어옴
df1 = pd.read_csv('oil.csv')
df2 = pd.read_csv('gasoline.csv')

# 두 데이터프레임을 공통된 열을 기준으로 병합
merged_df = pd.merge(df1, df2, on='Date', how='inner')

# 시각화
fig = px.line(merged_df, x='Date', y=['WTI', 'Brent', 'Dubai', 'Gasoline'],
              labels={'value': 'Prices(KRW/L)'})

# 시각화 보여주기
st.plotly_chart(fig, use_container_width=True)
