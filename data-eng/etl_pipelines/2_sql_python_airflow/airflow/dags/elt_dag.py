from datetime import datetime, timedelta
from airflow import DAG
from docker.types import Mount
# we import these two as we are using python and bash scripts
from airflow.operators.python_operator import PythonOperator
from aitflow.operators.bash import BashOperator

from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False
}

def run_elt_script():
    script_path = "/opt/airflow/elt_script.py"
    result = subprocess.run(["python", script_path], 
                            capture_output=True, 
                            text=True)
    
    if result.returncode != 0:
        raise Exception(f"script failed with Error: {result.stderr}")
    else:
        print(result.stdout)

dag = DAG(
    'elt_and_dbt',
    default_args=default_args,
    description='an ELT workflow with dbt',
    start_date=datetime(2023, 1, 25)
    catchup=False
)

# task1
t1 = PythonOperator(
    task_id="run_elt_script",
    python_callable=run_elt_script,
    dag=dag
)

# task2
t2 = DockerOperator(
    task_id='dbt_run',
    image='ghcr.io/dbt-labs/dbt-postgres:1.4.7',
    command=[
        "run",
        "--profiles-dir",
        "/root",
        "--project-dir",
        "/opt/dbt",
        "--full-refresh"
    ],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(source="/Users/Babak/DE-2/custom_postgres", target="/opt/dbt", type="bind"),
        Mount(source="/Users/Babak/.dbt", target="/root", type="bind")
    ],
    dag=dag
)

#   dbt:
#     image: ghcr.io/dbt-labs/dbt-postgres:1.4.7
#     # root => address of profile file for the dbt inside the docker container
#     # /dbt => address of the dbt directory inside the docker container
#     command:
#       [
#         "run",
#         "--profiles-dir",
#         "/root",
#         "--project-dir",
#         "/dbt",
#         "--full-refresh"
#       ]
#     networks:
#       - elt_network
#     depends_on:
#       - elt_script
#     environment:
#       DBT_PROFILE: default
#       DBT_TARGET: dev
#     volumes:
#       - ./custom_postgres:/dbt
#       - ~/.dbt:/root

# run task1 then task2
t1 >> t2


