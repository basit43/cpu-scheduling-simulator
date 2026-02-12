def sjf(processes):
    time = 0
    completed = []
    ready = []
    gantt = []

    while len(completed) < len(processes):
        for p in processes:
            if p.arrival <= time and p not in ready and p not in completed:
                ready.append(p)

        if ready:
            ready.sort(key=lambda x: x.burst)
            current = ready.pop(0)

            start = time
            time += current.burst
            end = time

            current.waiting = start - current.arrival
            current.turnaround = end - current.arrival

            gantt.append((current.pid, start, end))
            completed.append(current)
        else:
            time += 1

    return gantt