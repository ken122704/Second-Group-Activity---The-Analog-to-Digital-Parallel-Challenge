import time
import threading
from concurrent.futures import ThreadPoolExecutor

discharge_counter = 0
lock = threading.Lock()

def process_discharge(patient_id, use_lock=False):
    global discharge_counter

    time.sleep(0.01)  
    time.sleep(0.01)  
    time.sleep(0.01)  

    if use_lock:
        with lock:
            discharge_counter += 1
            discharge_id = discharge_counter
    else:
        discharge_counter += 1
        discharge_id = discharge_counter

    time.sleep(0.01) 

    return discharge_id

def run_sequential(patients):
    global discharge_counter
    discharge_counter = 0

    start = time.time()

    for p in patients:
        process_discharge(p, use_lock=False)

    end = time.time()
    return end - start
