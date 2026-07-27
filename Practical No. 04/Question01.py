n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = input(f"\nEnter Process ID (P{i+1}): ")
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    processes.append([pid, at, bt])

# Sort processes by Arrival Time
processes.sort(key=lambda x: x[1])

time = 0
total_wt = 0
total_tat = 0

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

gantt = []
times = [0]

for process in processes:
    pid, at, bt = process

    if time < at:
        time = at
        times[0] = time

    start = time
    time += bt
    ct = time
    tat = ct - at
    wt = tat - bt

    total_wt += wt
    total_tat += tat

    gantt.append(pid)
    times.append(ct)

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

print("\nAverage Waiting Time =", round(total_wt / n, 2), "ms")
print("Average Turnaround Time =", round(total_tat / n, 2), "ms")

print("\nGantt Chart:")
print("|", end="")
for p in gantt:
    print(f" {p} |", end="")
print()

for t in times:
    print(f"{t:<5}", end="")
print()
print("S117 Shravan Ramesh Vishwakarma")