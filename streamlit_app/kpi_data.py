import pandas as pd
import psycopg2

def get_kpi_data():
    conn = psycopg2.connect(
        host="ep-super-breeze-a27dvpse-pooler.eu-central-1.aws.neon.tech",  # Your Neon hostname
        port=5432,
        dbname="neondb",
        user="neondb_owner",              # Or your read-only user
        password="npg_EmR9jsW8lAau",      # Keep this in env var later
        sslmode="require"
    )
    df = pd.read_sql("""
        SELECT date_trunc('day', bet_time) AS date, COUNT(*) AS total_bets, 
               SUM(amount) AS total_amount, SUM(win) AS total_wins
        FROM bets
        GROUP BY 1
        ORDER BY 1 DESC
        LIMIT 30;
    """, conn)
    conn.close()
    return df
