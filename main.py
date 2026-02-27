from process_model import Process
from schedulers.fcfs import fcfs
from schedulers.sjf import sjf
from schedulers.round_robin import round_robin
from schedulers.srtf import srtf
import random
import copy
import matplotlib.pyplot as plt


def generate_random_processes(n, max_arrival=50, max_burst=10):
    processes = []
    for i in range(n):
        arrival = random.randint(0, max_arrival)
        burst = random.randint(1, max_burst)
        processes.append(Process(f"P{i}", arrival, burst))
    return processes


def plot_results(results):
    algorithms = list(results.keys())
    values = list(results.values())

    plt.bar(algorithms, values)
    plt.xlabel("Scheduling Algorithm")
    plt.ylabel("Average Waiting Time")
    plt.title("Average Waiting Time Comparison")
    plt.show()


def print_gantt(gantt, algorithm_name):
    print("\n" + "=" * 40)
    print(f"Algorithm: {algorithm_name}")
    print("=" * 40)
    print("Gantt Chart:")

    for pid, start, end in gantt:
        print(f"| {pid} ({start}-{end}) ", end="")

    print("|")
    print()


def run_experiment(n):
    print("\n" + "#" * 60)
    print(f"Running experiment with {n} random processes")
    print("#" * 60)

    base_workload = generate_random_processes(n)

    results = {}

    # FCFS
    processes = copy.deepcopy(base_workload)
    fcfs(processes)
    results["FCFS"] = sum(p.waiting for p in processes) / n

    # SJF (Non-preemptive)
    processes = copy.deepcopy(base_workload)
    sjf(processes)
    results["SJF"] = sum(p.waiting for p in processes) / n

    # SRTF (Preemptive SJF)
    processes = copy.deepcopy(base_workload)
    srtf(processes)
    results["SRTF"] = sum(p.waiting for p in processes) / n

    # Round Robin
    processes = copy.deepcopy(base_workload)
    round_robin(processes, quantum=3)
    results["RR (q=3)"] = sum(p.waiting for p in processes) / n

    return results

def run_multiple_trials(n, trials=5):
    aggregate = {"FCFS": 0, "SJF": 0, "SRTF": 0, "RR (q=3)": 0}

    for _ in range(trials):
        results = run_experiment(n)
        for key in aggregate:
            aggregate[key] += results[key]

    for key in aggregate:
        aggregate[key] /= trials

    return aggregate


def run_scalability_experiment(sizes, trials=5):
    scalability_results = {
        "FCFS": [],
        "SJF": [],
        "SRTF": [],
        "RR (q=3)": []
    }

    for n in sizes:
        print(f"\nRunning scalability test for N = {n}")

        aggregate = {
            "FCFS": 0,
            "SJF": 0,
            "SRTF": 0,
            "RR (q=3)": 0
        }

        for _ in range(trials):
            results = run_experiment(n)
            for key in aggregate:
                aggregate[key] += results[key]

        for key in aggregate:
            avg_value = aggregate[key] / trials
            scalability_results[key].append(avg_value)

    return scalability_results


def generate_heavy_tailed_processes(n, max_arrival=50, scale=10):
    processes = []
    for i in range(n):
        arrival = random.randint(0, max_arrival)

        # Exponential distribution
        burst = int(random.expovariate(1/scale))

        # Avoid zero burst
        burst = max(1, burst)

        processes.append(Process(f"P{i}", arrival, burst))

    return processes


def run_experiment(n, workload_type="heavy"):
    if workload_type == "uniform":
        base_workload = generate_random_processes(n)
    elif workload_type == "heavy":
        base_workload = generate_heavy_tailed_processes(n)
    else:
        raise ValueError("Unknown workload type")

    results = {}

    processes = copy.deepcopy(base_workload)
    fcfs(processes)
    results["FCFS"] = sum(p.waiting for p in processes) / n

    processes = copy.deepcopy(base_workload)
    sjf(processes)
    results["SJF"] = sum(p.waiting for p in processes) / n

    processes = copy.deepcopy(base_workload)
    srtf(processes)
    results["SRTF"] = sum(p.waiting for p in processes) / n

    processes = copy.deepcopy(base_workload)
    round_robin(processes, quantum=3)
    results["RR (q=3)"] = sum(p.waiting for p in processes) / n

    return results


def plot_scalability(sizes, scalability_results):
    for algo, values in scalability_results.items():
        plt.plot(sizes, values, marker='o', label=algo)

    plt.xlabel("Number of Processes (N)")
    plt.ylabel("Average Waiting Time")
    plt.title("Scalability Analysis of Scheduling Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()


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

# if __name__ == "__main__":

#     # Run experiment with 100 processes
#     # results = run_experiment(100)

#     # Run multiple Trials
#     results = run_multiple_trials(100, trials=5)


#     print("\nAverage Waiting Times:")
#     for algo, value in results.items():
#         print(f"{algo}: {value:.2f}")

#     plot_results(results)

if __name__ == "__main__":

    sizes = [50, 100, 200, 400]

    scalability_results = run_scalability_experiment(sizes, trials=5)

    print("\nScalability Results:")
    for algo, values in scalability_results.items():
        print(f"{algo}: {values}")

    plot_scalability(sizes, scalability_results)