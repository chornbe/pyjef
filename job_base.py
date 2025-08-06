import time
from datetime import datetime

class JobBase:
    def ping(self):
        raise NotImplementedError

    def shutdown(self):
        pass

    def name(self):
        return self.__class__.__name__

    def is_threaded(self) -> bool:
        raise NotImplementedError

    def log_job_start(self):
        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S.%f")[:-5]  # HH:MM:SS.t
        print(f"[{self.name()}] PING at {timestamp}")

class ThreadedJobBase(JobBase):
    def is_threaded(self):
        return True

class InlineJobBase(JobBase):
    def is_threaded(self):
        return False