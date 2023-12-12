import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_icon="📊",
    page_title="Tax Visualization",
    layout="wide"
)

st.title('Inventory and Consumption')


df = pd.read_csv('tax.csv')


fig = px.line(df, x='Date', y=['교통에너지환경세', '교육세', '주행'],
              labels={'value': 'Tax(KRW)'},
              title='Tax Components Over Time')


st.plotly_chart(fig)
