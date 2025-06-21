import ciw
import numpy as np

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    number_of_servers=[4],
)

WARMUP_TIME = 100
TARGET_TIME = 1440
COOLDOWN_TIME = 1000
SIMULATION_TIME = WARMUP_TIME + TARGET_TIME + COOLDOWN_TIME
average_waits = []
for trial_seed in range(10):
    ciw.seed(trial_seed)
    sim = ciw.Simulation(network)
    sim.simulate_until_max_time(SIMULATION_TIME)
    records = sim.get_all_records()
    waits = [
        record.waiting_time
        for record in records
        if record.arrival_date > WARMUP_TIME and
        record.arrival_date < SIMULATION_TIME - COOLDOWN_TIME
    ]
    mean_wait = np.mean(waits)
    average_waits.append(mean_wait)

print(np.mean(average_waits))
