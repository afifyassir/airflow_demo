from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "yassir",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(description="Our first DAG",
         dag_id="our_first_DAG_v5",
         schedule_interval="@daily",
         default_args=default_args,
         start_date=datetime(2024, 1, 8, 1)) as dag:

    task1 = BashOperator(task_id="task_1", bash_command="echo Hello World this the first task")

    task2 = BashOperator(task_id="task_2", bash_command="echo I am task two")

    task3 = BashOperator(task_id="task_3", bash_command="echo Hey I am task three and I will be running after task 1")

    # Task dependency method 1
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)

    # Task dependency method 2
    #task1 >> task2
    #task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]

    

