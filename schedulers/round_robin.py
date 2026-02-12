from collections import deque

def round_robin(processes, quantum):
    time = 0
    queue = deque()
    gantt = []

    processes = sorted(processes, key=lambda x: x.arrival)
    queue.append(processes[0])
    i = 1

    while queue:
        p = queue.popleft()

        start = time
        exec_time = min(quantum, p.remaining)
        p.remaining -= exec_time
        time += exec_time
        end = time

        gantt.append((p.pid, start, end))

        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        if p.remaining > 0:
            queue.append(p)
        else:
            p.turnaround = time - p.arrival
            p.waiting = p.turnaround - p.burst

    return gantt