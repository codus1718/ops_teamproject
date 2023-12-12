import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('gasoline_whole.csv')

st.title('--아직--')

st.set_page_config(
    page_icon="📊",
    page_title="Gasoline_whole",
    layout="wide"
)


fig = px.line(df, x='Date', y=['세전가',	'정유사', '대리점', '주유소'],
              labels={'value': 'Gasoline Price (KRW/L)'})


st.plotly_chart(fig, use_container_width=True)
