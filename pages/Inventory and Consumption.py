import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_icon="📊",
    page_title="Inventory and Consumption",
    layout="wide"
)

st.title('Inventory and Consumption')

df = pd.read_csv('consumption_inventory.csv')

fig = px.line(df, x='Date', y=['Inventory', 'Consumption'],
              labels={'value': 'Value'},
              title='Inventory and Consumption Over Time')


st.plotly_chart(fig, use_container_width=True)
