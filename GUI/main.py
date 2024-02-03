import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh



st.title('Pico_W專案123')
st.header('Pico :blue[cool] :sunglasses:', divider='red')
# st.divider()


url = 'https://blynk.cloud/external/api/get?token=d8JG7182JhgWt3s7_vLxWWliHzDmXEKY&v0&V1'
response = requests.request("GET",url)
if response.status_code ==200:
    all_data = response.json()
    st.info(f'光線:{all_data["v0"]}')
    st.warning(f'可變電阻:{all_data["V1"]}')
else:
    st.write("連線失敗，請稍後再試")
