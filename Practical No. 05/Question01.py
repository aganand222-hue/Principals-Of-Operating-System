import threading
from concurrent.futures import ThreadPoolExecutor

class SharedCounter:
    def __init__(self):
        self.completed_tasks = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.completed_tasks += 1

    def get_completed_tasks(self):
        with self.lock:
            return self.completed_tasks

def fibonacci_task(n, counter):
    print(f"\nThread: {threading.current_thread().name}")

    a, b = 0, 1
    print("Fibonacci Series:", end=" ")

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()

    counter.increment()

def main():
    counter = SharedCounter()

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(fibonacci_task, 10, counter)
        executor.submit(fibonacci_task, 12, counter)
        executor.submit(fibonacci_task, 15, counter)

    print("\nAll Tasks Completed.")
    print("Completed Tasks =", counter.get_completed_tasks())
    print("S117 Shravan Ramesh Vishwakarma")

if __name__ == "__main__":
    main()