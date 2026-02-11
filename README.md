# CPU Scheduling Simulator

A modular CPU Scheduling Simulator written in Python to explore and understand core Operating System scheduling algorithms.

This project simulates how an operating system decides which process runs on the CPU and in what order. It is designed to build strong foundations in systems thinking, scheduling theory, and performance evaluation.

---

## Implemented Algorithms

The simulator currently supports:

- **First Come First Serve (FCFS)** – Non-preemptive
- **Shortest Job First (SJF)** – Non-preemptive
- **Round Robin (RR)** – Preemptive (time-sliced)

Each algorithm is implemented independently in a modular structure for clarity and scalability.

---

## Project Structure

```text
CPU-SCHEDULING-SIMULATOR/
│
├── main.py
├── process_model.py
├── schedulers/
│   ├── __init__.py
│   ├── fcfs.py
│   ├── sjf.py
│   └── round_robin.py
│
└── README.md
