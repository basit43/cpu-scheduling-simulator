from process_model import Process
from schedulers.fcfs import fcfs
# Later:
from schedulers.sjf import sjf
from schedulers.round_robin import round_robin

def print_gantt(gantt):
    print("\nGantt Chart:")
    for pid, start, end in gantt:
        print(f"| {pid} ({start}-{end}) ", end="")
    print("|")


def fcfsProcess():
    return [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]
def sjfProcess():
    return [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]
def round_robin_process():
    return [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]

if __name__ == "__main__":
    processes = fcfsProcess()
    gantt = fcfs(processes)
    print_gantt(gantt)

    processes = sjfProcess()
    gantt = sjf(processes)
    print_gantt(gantt)

    processes = round_robin_process()
    gantt = round_robin(processes, quantum=2)
    print_gantt(gantt)