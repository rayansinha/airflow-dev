from airflow.decorators import dag
from datetime import datetime

@dag(
    start_date=datetime(2024,1,7),
    schedule='@daily',
    catchup=False,
    tags=['stock_market']
)
def stock_market():  # dag_id
    pass

stock_market()