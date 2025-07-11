import ciw

# M/M/3
network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=10)],
    service_distributions=[ciw.dists.Exponential(rate=10)],
    number_of_servers=[3],
)

NUM_CUSTOMERS = 30
ciw.seed(1)
sim = ciw.Simulation(network)
sim.simulate_until_max_customers(max_customers=NUM_CUSTOMERS, method="Finish")
