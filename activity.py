import time
import threading
from concurrent.futures import ThreadPoolExecutor

discharge_counter = 0
lock = threading.Lock()

def process_discharge(patient_id, use_lock=False):
    global discharge_counter

    # Simulate work stages
    time.sleep(0.01)  # Verify record
    time.sleep(0.01)  # Billing validation
    time.sleep(0.01)  # Insurance approval

    if use_lock:
        # Critical section (Parallel safe)
        with lock:
            discharge_counter += 1
            discharge_id = discharge_counter
    else:
        # Sequential version (no lock needed)
        discharge_counter += 1
        discharge_id = discharge_counter

    time.sleep(0.01)  # Generate summary

    return discharge_id
