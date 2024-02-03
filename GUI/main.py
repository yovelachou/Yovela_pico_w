import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
from dotenv import load_dotenv
import os

load_dotenv()

st_autorefresh(interval=5000)

st.title('Yovela的Pico_W專案')
st.header('Pico :blue[cool] :sunglasses:', divider='red')
# st.divider()


url = f'https://blynk.cloud/external/api/get?token={os.environ["API_KEY"]}&V0&V1'
response = requests.request("GET",url)
if response.status_code ==200:
    all_data = response.json()
    st.info(f'光線:{all_data["V0"]}')
    st.warning(f'可變電阻:{all_data["V1"]}')
else:
    st.write("連線失敗，請稍後再試")
