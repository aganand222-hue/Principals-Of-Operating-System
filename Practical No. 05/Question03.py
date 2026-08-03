import threading

def print_even():
    print("Even Numbers:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

def print_odd():
    print("Odd Numbers:")
    for i in range(1, 20, 2):
        print(i, end=" ")
    print()

def reverse_string(text):
    print("Original String:", text)
    print("Reversed String:", text[::-1])

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)
t3 = threading.Thread(target=reverse_string, args=("Multithreading",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nAll tasks completed.")
print("S117 Shravan Ramesh Vishwakarma")