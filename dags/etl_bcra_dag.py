from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from etl_bcra.extract_variables import extract_variables
from etl_bcra.transform_variables import transform_variables
from etl_bcra.extract_series import extract_series
from etl_bcra.transform_series import transform_series
from etl_bcra.db_utils import load_table, read_table

from sqlalchemy.exc import NoSuchTableError

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}


def etl_variables():
    variables_df = extract_variables()
    variables_df = transform_variables(variables_df)
    load_table(variables_df, "bcra_principales_variables")


def etl_series():
    variables_df = read_table("bcra_principales_variables")
    new_series_df = extract_series(variables_df)

    try:
        actual_series_df = read_table("bcra_series")
    except NoSuchTableError:
        print("NoSuchTableError: bcra_series")
        actual_series_df = None

    series_df = transform_series(actual_series_df, new_series_df)
    load_table(series_df, "bcra_series")


with DAG(
    'etl_bcra_dag',
    default_args=default_args,
    description='ETL pipeline del BRCA',
    schedule_interval='@daily',
    catchup=False,

) as dag:

    etl_variables_task = PythonOperator(
        task_id='etl_variables',
        python_callable=etl_variables
    )

    etl_series_task = PythonOperator(
        task_id='etl_series',
        python_callable=etl_series
    )

    etl_variables_task >> etl_series_task
