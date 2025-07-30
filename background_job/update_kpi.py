# Simulates a scheduled update job
from streamlit_app.kpi_data import get_kpi_data
df = get_kpi_data()
df.to_csv("streamlit_app/latest_kpis.csv", index=False)
print("Updated KPIs.")
