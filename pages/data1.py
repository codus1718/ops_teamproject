import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_icon="📊",
    page_title="GPV",
    layout="wide"
)

st.title('Supply And Demand')
st.write('')

df = pd.read_csv("supply_demand_refined.csv")


# 선 그래프 시각화
fig = px.line(df, x='Date', y=['Oil Import', 'Supply', 'Demand', 'Total Inventory'],
              labels={'value': 'Value'},
              title='Oil Data Over Time')

# 선 그래프를 streamlit에 표시
st.plotly_chart(fig)