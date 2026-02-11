def sjf(processes):
    time = 0
    completed = []
    ready = []
    schedule = []

    while len(completed) < len(processes):
        for p in processes:
            if p.arrival <= time and p not in ready and p not in completed:
                ready.append(p)

        if ready:
            ready.sort(key=lambda x: x.burst)
            current = ready.pop(0)
            schedule.append(current.pid)

            current.waiting = time - current.arrival
            time += current.burst
            current.turnaround = current.waiting + current.burst
            completed.append(current)
        else:
            time += 1

    return schedule