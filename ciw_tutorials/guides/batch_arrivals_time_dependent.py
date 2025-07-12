import ciw

class TimeDependentBatches(ciw.dists.Distribution):
    def sample(self, t: float = 0 , ind=None):
        if t < 10.0:
            return 2
        return 1

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Deterministic(value=3.0)],
    service_distributions=[ciw.dists.Deterministic(value=0.5)],
    batching_distributions=[TimeDependentBatches()],
    number_of_servers=[1],
)

sim = ciw.Simulation(network)
sim.simulate_until_max_time(16.0)
print(len(sim.nodes[-1].all_individuals))
