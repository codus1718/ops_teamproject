import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_icon="📊",
    page_title="Supply And Demand",
    layout="wide"
)

st.title('Supply And Demand')
st.write('')

df = pd.read_csv("supply_demand_refined.csv")


# 선 그래프 시각화
fig = px.lime(df, x='Date', y=['Oil Import', 'Supply', 'Demand', 'Total Inventory'],
              labels={'value': 'Amount of Oil(1k Bbl)'})

# 선 그래프를 streamlit에 표시
st.plotly_chart(fig, use_container_width=True)
