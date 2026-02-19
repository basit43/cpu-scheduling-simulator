def srtf(processes):
    time = 0
    completed = 0
    n = len(processes)
    gantt = []

    current_process = None

    while completed < n:

        # Get all arrived processes that are not finished
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]

        if ready:
            # Pick process with smallest remaining time
            ready.sort(key=lambda x: x.remaining)
            selected = ready[0]

            # If new process selected, add new gantt entry
            if current_process != selected:
                gantt.append((selected.pid, time, time + 1))
                current_process = selected
            else:
                # Extend last gantt entry
                last_pid, start, end = gantt[-1]
                gantt[-1] = (last_pid, start, end + 1)

            # Execute 1 time unit
            selected.remaining -= 1
            time += 1

            # If finished
            if selected.remaining == 0:
                selected.turnaround = time - selected.arrival
                selected.waiting = selected.turnaround - selected.burst
                completed += 1
        else:
            time += 1

    return gantt