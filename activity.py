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

def run_parallel(patients, num_threads=4):
    global discharge_counter
    discharge_counter = 0

    start = time.time()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda p: process_discharge(p, use_lock=True), patients)

    end = time.time()
    return end - start

if __name__ == "__main__":

    patients = list(range(300))

    print("Running Sequential Version...")
    sequential_time = run_sequential(patients)
    print("Sequential Time:", round(sequential_time, 4), "seconds")

    print("\nRunning Parallel Version (4 threads)...")
    parallel_time = run_parallel(patients, num_threads=4)
    print("Parallel Time:", round(parallel_time, 4), "seconds")

    speedup = sequential_time / parallel_time

    print("\nSpeedup:", round(speedup, 4))
