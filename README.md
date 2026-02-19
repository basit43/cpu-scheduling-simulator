# CPU Scheduling Simulator

A modular CPU Scheduling Simulator written in Python for exploring and experimentally evaluating classical Operating System scheduling algorithms.

This project goes beyond simple implementation by providing:

- Time-based Gantt chart simulation
- Detailed performance metrics
- Preemptive and non-preemptive scheduling
- Random workload generation
- Controlled experimental evaluation
- Statistical averaging across multiple trials
- Visualization using matplotlib

The simulator serves as a foundation for research-level exploration in scheduling theory and systems performance analysis.

---

## 🚀 Implemented Algorithms

The simulator currently supports:

- **First Come First Serve (FCFS)** – Non-preemptive  
- **Shortest Job First (SJF)** – Non-preemptive  
- **Shortest Remaining Time First (SRTF)** – Preemptive  
- **Round Robin (RR)** – Preemptive (time-sliced)

Each algorithm is implemented independently in a modular architecture for clarity, scalability, and future research extensions.

---

## 📊 Time-Based Gantt Chart Simulation

Each scheduler produces a detailed Gantt chart timeline showing:

- Execution order
- Start and end times
- Preemption events (SRTF, RR)
- Context switching behavior