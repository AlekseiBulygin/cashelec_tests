import threading
import time
import get_api


def help_func(lst, name):
    start_time_perc = time.time()
    result = get_api.get_api()
    lst.append(result[0])
    perc_time.append(time.time()-start_time_perc)
    print(name + ". Work is done")


if __name__ == "__main__":
    threads = []
    lst = []
    perc_time = []
    start_time = time.time()
    for i in range(8):
        name = f"Thread №{i}"
        thread = threading.Thread(target=help_func, args=(lst, name), name=name)
        print(thread.name + " is running")
        thread.start()
        threads.append(thread)

    print("Waiting...")

    for thread in threads:
        thread.join()
    proc_time = time.time() - start_time
    percentile_list = sorted([i for i in perc_time])
    percentile = percentile_list[round(len(percentile_list)*0.8) - 1]
    rps = round(len(lst) / proc_time)
    print("Complete proc.")
    if lst.count(200) == len(lst) and percentile < 0.45 and rps >= 5:
        print('Test is ok', f"rps = {rps}", '80% latency < 450 ms', sep='\n')
    else:
        print('Test is fail', f"rps = {rps}", '80% latency > 450 ms', sep='\n')
