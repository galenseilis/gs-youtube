import ciw

# M/M/1
network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(3)],
    service_distributions=[ciw.dists.Exponential(4)],
    number_of_servers=[10],
)

sim = ciw.Simulation(network)

sim.simulate_until_max_time(max_simulation_time=10_000, progress_bar=True)
