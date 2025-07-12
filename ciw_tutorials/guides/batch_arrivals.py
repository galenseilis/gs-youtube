import ciw

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Deterministic(value=18.5)],
    service_distributions=[ciw.dists.Deterministic(value=3.0)],
    batching_distributions=[ciw.dists.Deterministic(value=3)],
    number_of_servers=[1]
)

sim = ciw.Simulation(network)
sim.simulate_until_max_time(30.0)
recs = sim.get_all_records()
print(f"Arrival Times: {[r.arrival_date for r in recs]}")
print(f"Wait Times: {[r.waiting_time for r in recs]}")
