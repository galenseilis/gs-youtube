import ciw

# M/M/1
network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(1)],
    service_distributions=[ciw.dists.Exponential(1)],
    number_of_servers=[1],
)

ciw.seed(2025)

sim = ciw.Simulation(network)
sim.simulate_until_max_time(2)

records = sim.get_all_records()

print(records)

