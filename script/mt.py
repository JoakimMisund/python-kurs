import threading
import time

def process_stuff(name, start, stop):
    print(f"{name} started!")
    a = 0
    for i in range(start, stop):
        a += i**i
    print(f"{name} stopped!")
    return a

threads = []
calc_start = 0
calc_stop = 10000
num_threads = 5
chunk_size = (calc_stop - calc_start) // num_threads

s = time.time()
for i in range(num_threads):
    t = threading.Thread(
        target=process_stuff, args=(f"Thread-{i}", calc_start + chunk_size*i, calc_start + chunk_size*(i+1))
    )
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print(f"Processing time: {time.time() - s} seconds")