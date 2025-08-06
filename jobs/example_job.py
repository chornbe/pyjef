# jobs/example_job.py - shows how to get plugged in and fired up

from job_base import ThreadedJobBase
import time

class ExampleJob(ThreadedJobBase):
    def __init__(self):
        self._is_running = False
        self._last_run = None

    def ping(self):
        if self._is_running:
            return  # Already running, skip this ping

        self._is_running = True
        self._last_run = time.time()
        self.log_job_start()

        try:
            print(f"[{self.name()}] Starting threaded job...")
            time.sleep(0.5)
            print(f"[{self.name()}] Threaded job complete.")
        finally:
            self._is_running = False

    def shutdown(self):
        print(f"[{self.name()}] Shutting down.")
