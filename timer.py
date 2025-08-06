# timer.py - the raging heart, spitting at you from hell

import threading
from concurrent.futures import ThreadPoolExecutor

class RepeatingTimer:
    def __init__(self, jobs):
        self._timer = None
        self._is_running = False
        self._jobs = jobs
        self._executor = ThreadPoolExecutor(max_workers=10)

    def _run(self):
        if not self._is_running:
            return

        for job in self._jobs:
            try:
                if job.is_threaded():
                    self._executor.submit(job.ping)
                else:
                    job.ping()
            except Exception as e:
                print(f"[Timer] Error pinging job {job.name()}: {e}")

        self._start_timer()

    def _start_timer(self):
        self._timer = threading.Timer(1.0, self._run)
        self._timer.start()

    def start(self):
        if not self._is_running:
            self._is_running = True
            self._start_timer()

    def stop(self):
        self._is_running = False
        if self._timer:
            self._timer.cancel()
        self._executor.shutdown(wait=False)
        for job in self._jobs:
            try:
                job.shutdown()
            except Exception as e:
                print(f"[Timer] Error shutting down job {job.name()}: {e}")
