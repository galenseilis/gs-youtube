import ciw

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Deterministic(5)],
    service_distributions=[ciw.dists.Deterministic(4)],
    number_of_servers=[1],
)

if __name__ == "__main__":
    ciw.seed(0)
    sim = ciw.Simulation(network)
    sim.simulate_until_max_time(11)
    records = sim.get_all_records(include_incomplete=True)
    for record in records:
        print(record)
