import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('tax.csv')

st.set_page_config(
    page_icon="📊",
    page_title="Tax Visualization",
    layout="wide"
)


st.title('Tax Components Over Time')


fig = px.line(df, x='Date', y=['교통에너지환경세', '교육세', '주행세'],
              labels={'value': 'Tax(KRW)'})


st.plotly_chart(fig, use_container_width=True)
