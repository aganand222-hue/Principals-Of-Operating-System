n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = input(f"\nEnter Process ID (P{i+1}): ")
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    processes.append({
        "pid": pid,
        "at": at,
        "bt": bt,
        "ct": 0,
        "tat": 0,
        "wt": 0,
        "done": False
    })

time = 0
completed = 0
gantt = []
times = [0]

total_wt = 0
total_tat = 0

while completed < n:
    ready = [p for p in processes if p["at"] <= time and not p["done"]]

    if not ready:
        time += 1
        continue

    # Select process with shortest burst time
    ready.sort(key=lambda x: (x["bt"], x["at"]))
    p = ready[0]

    start = time
    time += p["bt"]

    p["ct"] = time
    p["tat"] = p["ct"] - p["at"]
    p["wt"] = p["tat"] - p["bt"]
    p["done"] = True

    total_wt += p["wt"]
    total_tat += p["tat"]

    gantt.append(p["pid"])
    times.append(time)

    completed += 1

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(processes, key=lambda x: x["pid"]):
    print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t{p['tat']}\t{p['wt']}")

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