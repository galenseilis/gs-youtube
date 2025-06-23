import ciw

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(10)],
    service_distributions=[ciw.dists.Exponential(10)],
    number_of_servers=[1],
    queue_capacities=[3],
)

ciw.seed(1)
sim = ciw.Simulation(network)
sim.simulate_until_max_customers(30, method='Finish')
records = sim.get_all_records()
print(len(records))
