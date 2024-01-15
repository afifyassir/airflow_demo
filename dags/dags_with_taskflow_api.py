from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    "owner": "yassir",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}


@dag(description="Our first DAG",
     dag_id="our_first_DAG_python_taskflow_api_v1",
     schedule_interval="@daily",
     default_args=default_args,
     start_date=datetime(2024, 1, 8, 1))
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {"first_name": "Ali", "last_name": "Ahmed"}

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello my name is {first_name} {last_name}"
              f"I am {age} years old")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict["first_name"], last_name=name_dict["last_name"], age=age)


greet_dag = hello_world_etl()
