# this here be the app loader. the kickstart. the fire-away button. The... you get it.

import argparse
import os
import time
from timer import RepeatingTimer
from job_loader import load_jobs

def main():
    # --------------------------------------------
    # CLI parsing for optional --jobs=... args
    # --------------------------------------------
    parser = argparse.ArgumentParser(description="Start the job timer application.")
    parser.add_argument(
        "--jobs",
        action="append",
        help="Path to a directory containing job modules. Can be passed multiple times.",
    )
    args = parser.parse_args()

    # Default to ./jobs if no --jobs flags are provided
    job_paths = args.jobs if args.jobs else ["./jobs"]
    job_paths = [os.path.expanduser(path) for path in job_paths]

    # Temporary debug output
    print(f"[App] Job search paths: {job_paths}")

    # --------------------------------------------
    # Load jobs from the first path only (for now)
    # --------------------------------------------
    jobs = load_jobs(job_paths[0])

    # --------------------------------------------
    # Start the timer (1-second interval, fixed)
    # --------------------------------------------
    timer = RepeatingTimer(jobs)
    timer.start()

    # --------------------------------------------
    # Keep the app running until user interrupts
    # --------------------------------------------
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[App] Shutting down...")
        timer.stop()
        print("[App] Done.")

if __name__ == "__main__":
    main()
