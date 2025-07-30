import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

@st.cache_data
def load_data():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=5432,
        sslmode="require"
    )
    query = "SELECT * FROM customer_kpis"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("📊 Customer KPI Dashboard")

df = load_data()

# Filters
pay_periods = df["pay_period"].dropna().unique()
selected_period = st.selectbox("Select Pay Period", sorted(pay_periods, reverse=True))

filtered = df[df["pay_period"] == selected_period]

st.metric("Total Customers", filtered["customer_id"].nunique())
st.metric("Total GGR", f"{filtered['ggr'].sum():,.2f}")
st.metric("Total NGR", f"{filtered['ngr'].sum():,.2f}")
st.metric("Total Deposits", f"{filtered['deposits'].sum():,.2f}")
st.metric("Total Withdrawals", f"{filtered['withdrawals'].sum():,.2f}")

st.dataframe(filtered)
