import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('gasoline_whole.csv')


st.write("열 이름:", df.columns)


st.set_page_config(
    page_icon="📊",
    page_title="Tax Visualization",
    layout="wide"
)


fig = px.line(df, x='Date', y=['교통에너지환경세', '교육세', '주행'],
              labels={'value': 'Value'},
              title='Tax Components Over Time')


st.plotly_chart(fig)
