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

class ThreadedJobBase(JobBase):
    def is_threaded(self):
        return True

class InlineJobBase(JobBase):
    def is_threaded(self):
        return False