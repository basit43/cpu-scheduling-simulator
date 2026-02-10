# CPU Scheduling Simulator

## Motivation
I built this project to better understand how CPU scheduling algorithms
work and what trade-offs they introduce in an operating system.

## Implemented Algorithms
- First Come First Serve (FCFS)
- Shortest Job First (Non-preemptive)
- Round Robin

## Metrics Observed
- Waiting time
- Turnaround time

## How it works
Each process is modeled with arrival time and burst time.
Schedulers simulate CPU execution step by step and calculate metrics.

## Observations
- FCFS is simple but can lead to long waiting times.
- SJF reduces average waiting time but may cause starvation.
- Round Robin improves fairness using time slicing.

## Limitations
- Single-core simulation
- No context switch overhead
- No I/O blocking

## Future Improvements
- Preemptive scheduling
- Context switch cost
- Visualization of schedules
