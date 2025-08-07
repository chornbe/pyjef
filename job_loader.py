import os
import importlib
import inspect
from pathlib import Path
from typing import List, Type
from job_base import JobBase

JOBS_PACKAGE = "jobs"
JOBS_PATH = Path(__file__).parent / JOBS_PACKAGE

def load_jobs(paths) -> List[JobBase]:
    job_instances = []

    for file in os.listdir(JOBS_PATH):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]  # Strip .py
            full_module = f"{JOBS_PACKAGE}.{module_name}"

            try:
                module = importlib.import_module(full_module)
            except Exception as e:
                print(f"[JobLoader] Failed to import module '{full_module}': {e}")
                continue

            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, JobBase) and obj is not JobBase:
                    try:
                        instance = obj()
                        job_instances.append(instance)
                        print(f"[JobLoader] Loaded job: {instance.name()}")
                    except Exception as e:
                        print(f"[JobLoader] Failed to instantiate '{obj.__name__}': {e}")

    return job_instances
