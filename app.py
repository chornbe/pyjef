# this here be the app loader. the kickstart. the fire-away button. The... you get it.

from timer import RepeatingTimer
from jobs.example_job import *
from jobs.example_job_2 import *
import time

if __name__ == "__main__":
    jobs = [
        ExampleJob(),
        ExampleJob2()
    ]
    timer = RepeatingTimer(jobs)
    timer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        timer.stop()
