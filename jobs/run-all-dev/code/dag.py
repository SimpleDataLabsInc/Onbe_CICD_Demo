import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from onbe_cicd_demo_run_all_models.tasks import Run_All_Models
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "Onbe_CICD_Demo_run_all_models", 
    schedule_interval = "0/1 * * * *", 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    params = {'DBT_TARGET' : Param("""DEV""", type = "string", title = """DBT_TARGET""")}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Run_All_Models_op = Run_All_Models()
