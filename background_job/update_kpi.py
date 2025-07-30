import psycopg2
import pandas as pd
import os
import time

def refresh_kpis():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=5432,
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        sslmode="require"
    )
    df = pd.read_sql("""
        SELECT date_trunc('day', bet_time) AS date,
               COUNT(*) AS total_bets,
               SUM(amount) AS total_amount,
               SUM(win) AS total_wins
        FROM bets
        GROUP BY 1
        ORDER BY 1 DESC
        LIMIT 30;
    """, conn)
    df.to_csv("streamlit_app/latest_kpis.csv", index=False)
    conn.close()
    print("Updated KPIs.")

while True:
    refresh_kpis()
    time.sleep(60)
