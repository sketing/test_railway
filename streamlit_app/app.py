# streamlit_app/app.py
import streamlit as st
from kpi_data import get_kpi_data

st.set_page_config(page_title="Dench KPI Dashboard (Live DB)", layout="wide")

st.title("📊 Dench KPI Dashboard (Live - Mode Analytics DB)")

df = get_kpi_data()

st.metric("📦 Orders Today", df['orders'].iloc[-1])
st.line_chart(df.set_index("date")["orders"])
