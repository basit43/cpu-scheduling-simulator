
class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.waiting = 0
        self.turnAround = 0
    
def fcfs(processes):
    time = 0
    gantt = []

    for p in sorted(processes, key=lambda x: x.arrival):
        if time < p.arrival:
            time = p.arrival

        start = time
        time += p.burst
        end = time

        p.waiting = start - p.arrival
        p.turnaround = end - p.arrival

        gantt.append((p.pid, start, end))

    return gantt

if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]

    print("FCFS:", fcfs(processes))