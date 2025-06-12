import ciw

ciw.seed(1)

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    number_of_servers=[3],
)

sim = ciw.Simulation(network)
sim.simulate_until_max_time(1440)
