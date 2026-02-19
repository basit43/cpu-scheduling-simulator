from process_model import Process
from schedulers.fcfs import fcfs
# Later:
from schedulers.sjf import sjf
from schedulers.round_robin import round_robin

def print_gantt(gantt, algorithm_name):
    print("\n" + "=" * 40)
    print(f"Algorithm: {algorithm_name}")
    print("=" * 40)
    print("Gantt Chart:")

    for pid, start, end in gantt:
        print(f"| {pid} ({start}-{end}) ", end="")

    print("|")
    print()

def print_metrics(processes, gantt):
    n = len(processes)

    avg_waiting = sum(p.waiting for p in processes) / n
    avg_turnaround = sum(p.turnaround for p in processes) / n

    # Context switches
    context_switches = 0
    for i in range(1, len(gantt)):
        if gantt[i][0] != gantt[i-1][0]:
            context_switches += 1

    print("\nMetrics:")
    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")
    print(f"Context Switches: {context_switches}")
    print()

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
    print_gantt(gantt, "FCFS")
    print_metrics(processes, gantt)

    processes = sjfProcess()
    gantt = sjf(processes)
    print_gantt(gantt, "SJF")
    print_metrics(processes, gantt)

    processes = round_robin_process()
    gantt = round_robin(processes, quantum=2)
    print_gantt(gantt, "Round Robin (q=2)")
    print_metrics(processes, gantt)