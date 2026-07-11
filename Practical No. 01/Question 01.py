from multiprocessing import Process, Semaphore, Lock, Array, Value, freeze_support
import random
import time

# Constants
BUFFER_SIZE = 5
ITEM_COUNT = 10


def producer(buffer, in_index, empty, full, mutex):
    print("Producer started", flush=True)

    for _ in range(ITEM_COUNT):
        item = random.randint(1, 100)

        # Wait for an empty slot
        empty.acquire()

        # Critical section
        with mutex:
            index = in_index.value
            buffer[index] = item
            print(f"Producer: Produced {item} at index {index}", flush=True)

            in_index.value = (index + 1) % BUFFER_SIZE

        # Signal that an item is available
        full.release()

        time.sleep(random.uniform(0.2, 0.5))


def consumer(buffer, out_index, empty, full, mutex):
    print("Consumer started", flush=True)

    for _ in range(ITEM_COUNT):
        # Wait until an item is available
        full.acquire()

        # Critical section
        with mutex:
            index = out_index.value
            item = buffer[index]
            print(f"Consumer: Consumed {item} from index {index}", flush=True)

            out_index.value = (index + 1) % BUFFER_SIZE

        # Signal that a buffer slot is free
        empty.release()

        time.sleep(random.uniform(0.2, 0.5))


def main():
    # Shared memory
    buffer = Array('i', BUFFER_SIZE)
    in_index = Value('i', 0)
    out_index = Value('i', 0)

    # Synchronization objects
    empty = Semaphore(BUFFER_SIZE)
    full = Semaphore(0)
    mutex = Lock()

    print("Starting Producer and Consumer...\n")

    producer_process = Process(
        target=producer,
        args=(buffer, in_index, empty, full, mutex)
    )

    consumer_process = Process(
        target=consumer,
        args=(buffer, out_index, empty, full, mutex)
    )

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("\nProducer and Consumer processes have finished.")
    print("S117 Shravan Ramesh Vishwakarma")

if __name__ == "__main__":
    freeze_support()      # Required for Windows
    main()

