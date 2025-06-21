import ciw
from numpy import block

network = ciw.create_network(
    arrival_distributions=[
        ciw.dists.Deterministic(value=4.0),
        None,
        None,
        ],
    service_distributions=[
        ciw.dists.Uniform(lower=3, upper=5),
        ciw.dists.Uniform(lower=3, upper=5),
        ciw.dists.Uniform(lower=3, upper=5),
        ],
    routing=[[0.0, 1.0, 0.0],
             [0.0, 0.0, 1.0],
             [0.0] * 3],
    number_of_servers=[1, 1, 1],
    queue_capacities=[3, 3, 3],
)

broken_stools = []
for trial in range(8):
    ciw.seed(trial)
    sim = ciw.Simulation(network)
    sim.simulate_until_max_time(4200)
    records = sim.get_all_records()
    num_broken = len([
        record.time_blocked
        for record in records
        if record.record_type == 'rejection' and
        record.arrival_date > 600
    ])
    broken_stools.append(num_broken)

print(broken_stools)

print(sum(broken_stools) / len(broken_stools))


network2 = ciw.create_network(
    arrival_distributions=[
        ciw.dists.Deterministic(value=4.0),
        None,
        None,
        ],
    service_distributions=[
        ciw.dists.Uniform(lower=3.5, upper=4.5),
        ciw.dists.Uniform(lower=3.5, upper=4.5),
        ciw.dists.Uniform(lower=3.5, upper=4.5),
        ],
    routing=[[0.0, 1.0, 0.0],
             [0.0, 0.0, 1.0],
             [0.0] * 3],
    number_of_servers=[1, 1, 1],
    queue_capacities=[3, 3, 3],
)

broken_stools = []
for trial in range(8):
    ciw.seed(trial)
    sim = ciw.Simulation(network2)
    sim.simulate_until_max_time(4200)
    records = sim.get_all_records()
    num_broken = len([
        record.time_blocked
        for record in records
        if record.record_type == 'rejection' and
        record.arrival_date > 600
    ])
    broken_stools.append(num_broken)

print(broken_stools)

print(sum(broken_stools) / len(broken_stools))
