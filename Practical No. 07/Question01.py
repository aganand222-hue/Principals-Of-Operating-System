import threading
import time
import random

BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE

in_pos = 0
out_pos = 0

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)


def producer():
    global in_pos

    for item in range(1, 11):
        empty.acquire()
        mutex.acquire()

        buffer[in_pos] = item
        print("Produced:", item, "at position", in_pos)

        in_pos = (in_pos + 1) % BUFFER_SIZE

        mutex.release()
        full.release()

        time.sleep(random.uniform(0.2, 0.5))


def consumer():
    global out_pos

    for i in range(1, 11):
        full.acquire()
        mutex.acquire()

        item = buffer[out_pos]
        buffer[out_pos] = None

        print("Consumed:", item, "from position", out_pos)

        out_pos = (out_pos + 1) % BUFFER_SIZE

        mutex.release()
        empty.release()

        time.sleep(random.uniform(0.3, 0.6))


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("\nProduction and consumption completed.")
print("S117 Shravan Ramesh Vishwakarma")