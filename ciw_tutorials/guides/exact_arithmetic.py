import ciw

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(5)],
    service_distributions=[ciw.dists.Exponential(10)],
    number_of_servers=[1],
)


ciw.seed(2)
sim = ciw.Simulation(network, exact=26)
sim.simulate_until_max_time(100.0)
waits = [record.waiting_time for record in sim.get_all_records()]
print(waits[-1])
