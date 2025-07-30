import pandas as pd
import datetime
import random

def get_kpi_data():
    today = datetime.date.today()
    data = {
        "date": [today - datetime.timedelta(days=i) for i in range(30)][::-1],
        "users": [random.randint(100, 500) for _ in range(30)],
    }
    return pd.DataFrame(data)
