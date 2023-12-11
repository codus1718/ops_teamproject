import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_icon="📊",
    page_title="Team 6",
    layout="wide"
)


st.title('Combined Price Trends of WTI, Brent, Dubai, and Gasoline')


# 두 개의 CSV 파일을 읽어옴
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# 두 데이터프레임을 공통된 열을 기준으로 병합
merged_df = pd.merge(df1, df2, on='common_column_name', how='inner')

# 시각화
fig = px.line(merged_df, x='Date', y=['WTI', 'Brent', 'Dubai', 'Gasoline'],
              labels={'value': 'Value'},
              title='Combined Visualization of WTI, Brent, Dubai, and Gasoline')

# 시각화 보여주기
fig.show()
