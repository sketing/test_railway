import psycopg2
import random
from datetime import datetime
import os
import time

def insert_fake_bet():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=5432,
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        sslmode="require"
    )
    cur = conn.cursor()

    user_id = random.randint(1, 1000)
    session_id = random.randint(1, 10000)
    amount = round(random.uniform(1.0, 50.0), 2)
    win = round(amount * random.uniform(0, 2), 2)
    game = random.choice(["slots", "blackjack", "roulette", "poker"])
    bet_time = datetime.now()

    cur.execute("""
        INSERT INTO bets (user_id, session_id, amount, win, game, bet_time)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (user_id, session_id, amount, win, game, bet_time))

    conn.commit()
    conn.close()
    print(f"Inserted fake bet at {bet_time}")

while True:
    insert_fake_bet()
    time.sleep(30)
