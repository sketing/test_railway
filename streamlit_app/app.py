import streamlit as st
import pandas as pd
from kpi_data import get_kpi_data

st.set_page_config(page_title="Dench KPI Dashboard", layout="wide")

st.title("📊 Dench KPI Dashboard (Demo)")

df = get_kpi_data()

st.metric("📈 Active Users Today", df['users'].iloc[-1])
st.line_chart(df.set_index("date")["users"])
