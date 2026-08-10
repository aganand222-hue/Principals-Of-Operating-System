from collections import deque

def round_robin(processes, arrival, burst, quantum):
    n = len(processes)
    remaining = burst.copy()
    completion = [0] * n
    first_start = [-1] * n

    time = 0
    completed = 0
    queue = deque()
    added = [False] * n

    while completed < n:

        for i in range(n):
            if arrival[i] <= time and not added[i]:
                queue.append(i)
                added[i] = True

        if not queue:
            time += 1
            continue

        i = queue.popleft()

        if first_start[i] == -1:
            first_start[i] = time

        execution = min(quantum, remaining[i])
        time += execution
        remaining[i] -= execution

        for j in range(n):
            if arrival[j] <= time and not added[j]:
                queue.append(j)
                added[j] = True

        if remaining[i] > 0:
            queue.append(i)
        else:
            completion[i] = time
            completed += 1

    turnaround = [completion[i] - arrival[i] for i in range(n)]
    waiting = [turnaround[i] - burst[i] for i in range(n)]

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

    for i in range(n):
        print(f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t"
              f"{completion[i]}\t{turnaround[i]}\t{waiting[i]}")

    print("\nAverage Turnaround Time:",
          round(sum(turnaround) / n, 2), "ms")

    print("Average Waiting Time:",
          round(sum(waiting) / n, 2), "ms")

n = int(input("Enter number of processes: "))

processes = []
arrival = []
burst = []

for i in range(n):
    processes.append("P" + str(i + 1))
    arrival.append(int(input(f"Enter arrival time of P{i + 1}: ")))
    burst.append(int(input(f"Enter burst time of P{i + 1}: ")))

quantum = int(input("Enter time quantum: "))

round_robin(processes, arrival, burst, quantum)
print("S117 Shravan Ramesh Vishwakarma")