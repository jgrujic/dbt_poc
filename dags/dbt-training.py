from airflow import DAG
from datafy.factories import DatafyDbtTaskFactory
from datetime import datetime, timedelta
from datafy.secrets import AWSParameterStoreValue

project_name = "dbt_poc"
environment = "{{ macros.datafy.env() }}"
aws_role = f"neo-iam-{project_name.replace('_', '')}-dev"

default_args = {
    "owner": "Datafy",
    "depends_on_past": False,
    "start_date": datetime(year=2022, month=1, day=18),
    "email": [],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


dag = DAG(
    "dbt-training", default_args=default_args, schedule_interval="@daily", max_active_runs=1
)

factory = DatafyDbtTaskFactory(
    task_aws_role=aws_role,
    task_env_vars={"REMOTE_DBT_HOST": AWSParameterStoreValue(name="/project/dev/dbtpoc/dtbtraining_host"), 
                   "REMOTE_DBT_USER": AWSParameterStoreValue(name="/project/dev/dbtpoc/dtbtraining_user"), 
                   "REMOTE_DBT_PWD": AWSParameterStoreValue(name="/project/dev/dbtpoc/training_password"),},
    task_arguments=["--no-use-colors", "{command}", "--target", "{{ macros.datafy.env() }}", "--profiles-dir", "./..", "--select", "{model}", "--vars", '{"date": {{ ds }}, "num_days": 1}']
)
factory.add_tasks_to_dag(dag=dag)
