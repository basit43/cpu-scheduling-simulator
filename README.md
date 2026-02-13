# CPU Scheduling Simulator

A modular CPU Scheduling Simulator written in Python to explore and understand core Operating System scheduling algorithms through time-based simulation and performance evaluation.

This project models how an operating system decides which process runs on the CPU and in what order. It provides execution order, detailed metrics, and **Gantt chart timeline visualization** to analyze scheduling behavior.

---

## 🚀 Implemented Algorithms

The simulator currently supports:

- **First Come First Serve (FCFS)** – Non-preemptive  
- **Shortest Job First (SJF)** – Non-preemptive  
- **Round Robin (RR)** – Preemptive (time-sliced)

Each algorithm is implemented independently in a modular structure for clarity, scalability, and future research-level extensions.

---

## 📊 Gantt Chart Visualization

The simulator generates a **Gantt Chart timeline** for each scheduling algorithm.

The Gantt chart visually represents:

- Execution order  
- Start and end times  
- Preemption (for Round Robin)  
- Context switching behavior  

Example (conceptual output):



This helps in reasoning about:

- CPU utilization  
- Waiting time accumulation  
- Fairness  
- Scheduling trade-offs  
- Time-based system behavior  

---

## 📈 Performance Metrics Tracked

Each process tracks:

- Arrival Time  
- Burst Time  
- Remaining Time  
- Waiting Time  
- Turnaround Time  

Where:


These metrics are fundamental for evaluating scheduling efficiency and comparing algorithms.

---

## 🧠 Scheduling Concepts Covered

### 1️⃣ First Come First Serve (FCFS)
- Executes processes in order of arrival  
- Simple and deterministic  
- Can suffer from the **convoy effect**  

### 2️⃣ Shortest Job First (SJF)
- Selects process with smallest burst time  
- Minimizes average waiting time  
- May cause starvation for long processes  

### 3️⃣ Round Robin (RR)
- Uses fixed time quantum  
- Ensures fairness and responsiveness  
- Introduces context switching overhead  

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
│   └── round_robin.py
│
└── README.md