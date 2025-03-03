import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from onbe_cicd_demo_run_all_dev.tasks import dev
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "onbe_cicd_demo_run_all_dev", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    params = {'env_dev' : Param("""DEV""", type = "string", title = """env_dev""")}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2025, 3, 20, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    dev_op = dev()
