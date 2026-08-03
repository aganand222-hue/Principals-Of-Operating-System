import threading

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")

numbers = [5, 7, 10, 4]

threads = []

for num in numbers:
    thread = threading.Thread(target=factorial, args=(num,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nAll factorial calculations completed.")
print("S117 Shravan Ramesh Vishwakarma")