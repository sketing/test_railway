import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# --- Load environment variables ---
DATABASE_URL = os.getenv("DATABASE_URL")

# --- Create DB engine ---
engine = create_engine(DATABASE_URL)

# --- Streamlit setup ---
st.set_page_config(page_title="DEMOCustomer KPI Dashboard", layout="wide")
st.title("📊 DEMO Customer KPI Dashboard")

# --- Query data ---
query = "SELECT * FROM customer_kpis"
df = pd.read_sql(query, engine)

# --- KPI summary ---
st.subheader("📌 KPI Summary")
col1, col2, col3 = st.columns(3)
col1.metric("🧍 Unique Customers", df["customer_id"].nunique())
col2.metric("💰 Total GGR", f"€{df['ggr'].sum():,.2f}")
col3.metric("💸 Total NGR", f"€{df['ngr'].sum():,.2f}")

# --- Time-series chart ---
st.subheader("📈 NGR & GGR Over Time")
df["pay_period"] = pd.to_datetime(df["pay_period"])
df_sorted = df.sort_values("pay_period")
line_data = df_sorted.groupby("pay_period")[["ggr", "ngr"]].sum()

st.line_chart(line_data)
