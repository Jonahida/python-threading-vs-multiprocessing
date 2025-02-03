import threading
import multiprocessing
import time

N = 10**7  # Number of iterations for the test


def cpu_task(n):
    """Performs a CPU-intensive task"""
    sum_result = sum(i * i for i in range(n))


def measure_threading_time():
    start = time.time()

    thread1 = threading.Thread(target=cpu_task, args=(N,))
    thread2 = threading.Thread(target=cpu_task, args=(N,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end = time.time()
    print(f"Time with threading: {end - start:.2f} seconds")


def measure_multiprocessing_time():
    start = time.time()

    process1 = multiprocessing.Process(target=cpu_task, args=(N,))
    process2 = multiprocessing.Process(target=cpu_task, args=(N,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()
    print(f"Time with multiprocessing: {end - start:.2f} seconds")


if __name__ == "__main__":
    print(f"Running test with {N} iterations")
    measure_threading_time()
    measure_multiprocessing_time()

