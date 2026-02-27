# CPU Scheduling Simulator

A modular CPU Scheduling Simulator written in Python for experimental evaluation of classical Operating System scheduling algorithms.

This project models how an operating system selects processes for CPU execution and analyzes algorithm behavior under different workload conditions.

It supports:

- Time-based Gantt chart simulation
- Preemptive and non-preemptive scheduling
- Detailed performance metrics
- Random workload generation (uniform & heavy-tailed)
- Multi-trial statistical averaging
- Scalability experiments
- Visualization using matplotlib

The simulator is designed as a foundation for research-oriented systems analysis.

---

## 🚀 Implemented Scheduling Algorithms

The simulator currently supports:

- **First Come First Serve (FCFS)** – Non-preemptive  
- **Shortest Job First (SJF)** – Non-preemptive  
- **Shortest Remaining Time First (SRTF)** – Preemptive  
- **Round Robin (RR)** – Preemptive (time-sliced)

Each algorithm is implemented independently within a modular architecture for clarity and extensibility.

---

## 📊 Gantt Chart Simulation

Each scheduler produces a detailed Gantt chart timeline that shows:

- Execution order
- Start and end times
- Preemption events (SRTF and RR)
- Context switching behavior

Example:

========================================
Algorithm: SRTF
Gantt Chart:
| P1 (0-1) | P2 (1-4) | P1 (4-8) | ...


This enables precise time-based reasoning about scheduling behavior.

---

## 📈 Performance Metrics

For every experiment, the simulator computes:

- Average Waiting Time
- Average Turnaround Time
- Context Switch Count

Each process tracks:

- Arrival Time
- Burst Time
- Remaining Time
- Waiting Time
- Turnaround Time

These metrics enable quantitative comparison between scheduling strategies.

---

## 🔬 Experimental Evaluation Framework

The simulator supports controlled experiments:

- Generate N processes
- Use identical workloads across all algorithms
- Run multiple trials
- Compute averaged results
- Visualize comparisons

Two workload models are supported:

### 1️⃣ Uniform Workload
Burst times generated using uniform distribution.

### 2️⃣ Heavy-Tailed Workload
Burst times generated using exponential distribution to simulate realistic systems behavior (many short jobs, few long jobs).

---

## 📊 Scalability Analysis

The simulator evaluates scalability across increasing workload sizes:

N = [50, 100, 200, 400]


It produces scalability curves showing:

- Growth of average waiting time vs number of processes
- Performance divergence between algorithms
- Sensitivity to workload distribution

### Observed Experimental Trends

Under uniform workloads:

- SRTF ≈ SJF < FCFS < RR
- All algorithms scale approximately linearly

Under heavy-tailed workloads:

- SRTF shows clearer advantage
- FCFS suffers severe convoy effect
- RR performance degrades significantly under scale
- Performance gaps widen as N increases

These results align with theoretical scheduling expectations.

---

## 📂 Project Structure

```text
CPU-SCHEDULING-SIMULATOR/
│
├── main.py
├── process_model.py
├── schedulers/
│   ├── __init__.py
│   ├── fcfs.py
│   ├── sjf.py
│   ├── srtf.py
│   └── round_robin.py
│
├── requirements.txt
└── README.md

Create virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python main.py