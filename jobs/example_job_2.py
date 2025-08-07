from job_base import InlineJobBase
import time

class ExampleJob2(InlineJobBase):
    def __init__(self):
        self._is_running = False
        self._last_run = None

    def ping(self):
        self._is_running = True
        self._last_run = time.time()
        print(f"[{self.name()}] Doing inline work...")
        time.sleep(0.25)
        print(f"[{self.name()}] Finished inline work.")
        self._is_running = False

    def shutdown(self):
        print(f"[{self.name()}] Shutting down.")
