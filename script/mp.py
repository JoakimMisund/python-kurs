import multiprocessing
import time

def process_stuff(name, start, stop):
    print(f"{name} started!")
    a = 0
    for i in range(start, stop):
        a += i**i
    print(f"{name} stopped!")
    return a

if __name__ == '__main__':
    processes = []
    calc_start = 0
    calc_stop = 10000
    num_procs = 5
    chunk_size = (calc_stop - calc_start) // num_procs

    s = time.time()
    for i in range(num_procs):
        p = multiprocessing.Process(
            target=process_stuff, args=(f"Proc-{i}", calc_start + chunk_size*i, calc_start + chunk_size*(i+1))
        )
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    print(f"Processing time: {time.time() - s} seconds")