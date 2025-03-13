from _0qytbn7imajrwaeacbx9uq_.utils import *

def dev():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "dev",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": True,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": False,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": "42856",
          "git_entity": "branch",
          "git_entity_value": None,
          "git_ssh_url": "https://github.com/SimpleDataLabsInc/Onbe_CICD_Demo",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile --vars {\"env\":\"{{ params.env_dev }}\"}",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy"}, 
          "git_token_secret": "_NtjBb4zgHIz_motVpzuEg_", 
          "dbt_profile_secret": "NzOYOhrwZlUSnUcoXeZlb"
        },
    )
