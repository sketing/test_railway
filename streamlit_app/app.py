import streamlit as st
from kpi_data import get_kpi_data

st.set_page_config(page_title="🎰 Dench KPI Dashboard", layout="wide")

st.title("📊 Dench KPI Dashboard (Neon DB)")

df = get_kpi_data()

st.metric("🎯 Bets Today", int(df['total_bets'].iloc[0]))
st.metric("💸 Total Amount", f"€{df['total_amount'].iloc[0]:,.2f}")
st.metric("🎉 Total Winnings", f"€{df['total_wins'].iloc[0]:,.2f}")

st.line_chart(df.set_index("date")[["total_amount", "total_wins"]])
