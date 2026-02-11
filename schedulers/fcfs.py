print("SCRIPT STARTED")
#showing python editor version
import sys
print("Python editor version:", sys.version_info)
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
    schedule = []
    for p in sorted(processes, key=lambda x: x.arrival):
        if time < p.arrival:
            time = p.arrival

        p.waiting = time - p.arrival
        time += p.burst
        p.turnaround = p.waiting + p.burst
        schedule.append(p.pid)

    return schedule

if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]

    print("FCFS:", fcfs(processes))