import ciw

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(10)],
    service_distributions=[ciw.dists.Exponential(10)],
    number_of_servers=[1],
    queue_capacities=[3],
)

ciw.seed(1)
sim = ciw.Simulation(network)
sim.simulate_until_max_customers(30, method="Accept")
records = sim.get_all_records()
print(
    len([r for r in records if r.record_type == "service"]),
    len(sim.nodes[1].all_individuals),
    len([r for r in records if r.record_type == "rejection"]),
)
