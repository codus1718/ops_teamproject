import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_icon="📊",
    page_title="Types of Crude Oil",
    layout="wide"
)


st.title('Combined Price Trends of WTI, Brent, Dubai, and Gasoline')


# 두 개의 CSV 파일을 읽어옴
df1 = pd.read_csv('oil.csv')
df2 = pd.read_csv('gasoline.csv')

# 두 데이터프레임을 공통된 열을 기준으로 병합
merged_df = pd.merge(df1, df2, on='Date', how='inner')

# 시각화
fig = px.line(merged_df, x='Date', y=['WTI', 'Brent', 'Dubai', 'Gasoline'],
              labels={'value': 'Prices(KRW/L)'})

# 시각화 보여주기
st.plotly_chart(fig, use_container_width=True)

st.write('WTI (West Texas Intermediate): 미국 텍사스 주 서부 지역에서 채취되는 원유. WTI는 가장 널리 거래되는 석유 지표 중 하나이며, 미국에서 소비되는 석유 제품 가격에 영향을 미침.')

st.write('Brent: 북해 지역에서 채취되는 원유. Brent는 유럽과 아시아 지역에서 사용되는 주요 석유 지표 중 하나이며, 국제적으로 중요한 기준 지표 중 하나로 간주됨.')

st.write('Dubai: 중동 지역에서 채취되는 원유. Dubai 원유는 주로 중동 지역에서 소비되는 석유 제품 가격을 결정하는 데 사용됨')
