import threading
import time

# Simulates a time-consuming function
def task(name):
    print(f"{name} started")
    time.sleep(2)  # Simulates work by pausing for 2 seconds
    print(f"{name} finished")

print("\n--- Sequential Execution ---")
start_time = time.time()
task("Task 1")
task("Task 2")
end_time = time.time()
print("Sequential Execution Time:", round(end_time - start_time, 2), "seconds")

print("\n--- Threaded Execution ---")
start_time = time.time()
# Create threads
t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))
# Start both threads
t1.start()
t2.start()
# Wait for both threads to finish
t1.join()
t2.join()
end_time = time.time()

print("Threaded Execution Time:", round(end_time - start_time, 2), "seconds")
print("S117 Shravan Ramesh Vishwakarma")