# streamlit_app/kpi_data.py
import pandas as pd
import psycopg2

def get_kpi_data():
    conn = psycopg2.connect(
        host="tutorial-db.modeanalytics.com",
        port=5432,
        dbname="modeanalytics",
        user="mode",
        password="mode"
    )
    query = """
        SELECT order_date::date AS date, COUNT(*) AS orders
        FROM tutorial.orders
        GROUP BY 1
        ORDER BY 1
        LIMIT 30;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df
