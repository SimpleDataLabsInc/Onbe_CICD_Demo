from best_neil_onbe_cicd_demo_run_all_dev.utils import *

def Check_DBT_Target():

    def check_dbt_target():
        from airflow.models import Variable

        if Variable.get("AIRFLOW_INSTANCE_ENV") == "{{ params.DBT_TARGET }}":
            return "Run_All_Models"
        else:
            return None

    from datetime import timedelta
    from airflow.operators.python import BranchPythonOperator

    return BranchPythonOperator(task_id = "Check_DBT_Target", python_callable = check_dbt_target, )
