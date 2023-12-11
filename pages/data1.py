import streamlit as st

st.set_page_config(
    page_icon="📊",
    page_title="GPV",
    layout="wide"
)

st.title('Supply And Demand')
st.write('')

data = pd.read_csv("supply_demand_refined.csv")
