import ciw

network = ciw.create_network(
    arrival_distributions={
        'class 0': [ciw.dists.Deterministic(value=18.5)],
        'class 1': [ciw.dists.Deterministic(value=10.5)],
    },
    service_distributions={
        'class 0': [ciw.dists.Deterministic(value=3.0)],
        'class 1': [ciw.dists.Deterministic(value=6.0)],
    },
    batching_distributions={
        'class 0': [ciw.dists.Deterministic(value=3)],
        'class 1': [ciw.dists.Deterministic(value=100)],
    },
    number_of_servers=[1]
)

sim = ciw.Simulation(network)
sim.simulate_until_max_time(1000.0)
recs = sim.get_all_records()
print(f"Arrival Times: {[r.arrival_date for r in recs]}")
print(f"Wait Times: {[r.waiting_time for r in recs]}")
