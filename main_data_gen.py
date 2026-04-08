import numpy as np
import os

def parse_mk_data(file_path):
    with open(file_path, 'r') as f:
        raw_data = f.read()
    lines = [line.strip() for line in raw_data.split('\n') if line.strip()]
    header = list(map(float, lines[0].split()))
    num_jobs, num_machines = int(header[0]), int(header[1])
    jobs = []
    for line in lines[1:]:
        data = list(map(int, line.strip().split()))
        op_count = data[0]
        ptr = 1
        operations = []
        for _ in range(op_count):
            machine_options = data[ptr]
            ptr += 1
            machines = []
            times = []
            for _ in range(machine_options):
                machine = data[ptr] - 1
                time = data[ptr + 1]
                machines.append(machine)
                times.append(time)
                ptr += 2
            operations.append({'machines': machines, 'times': times})
        jobs.append(operations)
    return jobs, num_jobs, num_machines

def generate_cost_and_due_dates(jobs, num_jobs, num_machines, alpha_range=(1.5, 3.0), beta=3, seed=42):
    if seed is not None:
        np.random.seed(seed)
    INF = 9999
    max_ops = max(len(job) for job in jobs)
    machine_times = [[[INF] * num_machines for _ in range(max_ops)] for _ in range(num_jobs)]
    machine_costs = [[[INF] * num_machines for _ in range(max_ops)] for _ in range(num_jobs)]
    due_dates = []
    for job_idx, job in enumerate(jobs):
        base_time = 0
        for op_idx, op in enumerate(job):
            valid_machines = op['machines']
            times = op['times']
            for m, t in zip(valid_machines, times):
                machine_times[job_idx][op_idx][m] = t
                alpha = np.random.uniform(*alpha_range)
                cost = t * alpha * np.random.uniform(0.9, 1.1) * 1
                machine_costs[job_idx][op_idx][m] = round(cost, 1)
            base_time += min(times)
        due_date = int(base_time * (1 + beta * np.random.rand()))
        due_dates.append(due_date)
    return machine_times, machine_costs, due_dates

if __name__ == "__main__":
    data_dir = './data'
    output_dir = './augmented_data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, 11):
        file_name = f'MK{i:02d}.txt'
        file_path = os.path.join(data_dir, file_name)
        if os.path.exists(file_path):
            print(f"Processing {file_name}...")
            jobs, n_j, n_m = parse_mk_data(file_path)
            times, costs, dues = generate_cost_and_due_dates(jobs, n_j, n_m)
            
            np.save(os.path.join(output_dir, f'mk{i:02d}_costs.npy'), costs)
            np.save(os.path.join(output_dir, f'mk{i:02d}_dues.npy'), dues)
