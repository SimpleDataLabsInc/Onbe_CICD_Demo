import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from _0qytbn7imajrwaeacbx9uq_.tasks import dev
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "0qyTBN7imaJRWaeACBX9UQ_", 
    schedule_interval = "0/1 * * * *", 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "MIio4Toq"}, 
    params = {'env_dev' : Param("""DEV""", type = "string", title = """env_dev""")}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2025, 3, 20, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    dev_op = dev()
