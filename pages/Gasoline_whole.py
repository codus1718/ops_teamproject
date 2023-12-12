import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('gasoline_whole.csv')

st.set_page_config(
    page_icon="📊",
    page_title="Gasoline_whole",
    layout="wide"
)

st.title('Comparison of Oil Prices among Refinery, Distributor, Agent, and Gas Statio')
st.write('세전가 : 어떤 상품이나 서비스의 가격에 세금이나 부가가치세(VAT)를 포함하지 않은 가격')
st.write('정유사 :  정제된 석유 제품을 생산하는 회사나 시설을 가리키는 한국어 용어')




fig = px.line(df, x='Date', y=['세전가',	'정유사', '대리점', '주유소'],
              labels={'value': 'Gasoline Price (KRW/L)'})


st.plotly_chart(fig, use_container_width=True)
