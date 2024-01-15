from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


def greet(ti):
    first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
    last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
    age = ti.xcom_pull(task_ids="get_age", key="age")
    print(f"Hello World, my name is {first_name} {last_name},"
          f"and I am {age} old")


def get_name(ti):
    ti.xcom_push(key="first_name", value="Ali")
    ti.xcom_push(key="last_name", value="Ahmed")


def get_age(ti):
    ti.xcom_push(key="age", value=20)


default_args = {
    "owner": "yassir",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(description="Our first DAG",
         dag_id="our_first_DAG_python_v3",
         schedule_interval="@daily",
         default_args=default_args,
         start_date=datetime(2024, 1, 8, 1)) as dag:

    task1 = PythonOperator(task_id="get_name", python_callable=get_name)

    task2 = PythonOperator(task_id="get_age", python_callable=get_age)

    task3 = PythonOperator(task_id="greet",
                           python_callable=greet
                           # op_kwargs={"name": "Ali"}
                           )
    [task1, task2] >> task3 
