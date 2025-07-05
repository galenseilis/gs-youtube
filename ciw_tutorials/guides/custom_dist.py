import ciw
import random

class CustomDistribution(ciw.dists.Distribution):
    def sample(self, t=None, ind=None):
        if random.random() < 0.5:
            return 3.0
        return random.random()

class AnotherCustomDistribution(ciw.dists.Distribution):
    def sample(self, t=None, ind=None):
        if random.random() < 0.7:
            return 3.0
        return random.random() * 100

network = ciw.create_network(
    arrival_distributions=[AnotherCustomDistribution()],
    service_distributions=[CustomDistribution()],
    number_of_servers=[10],
)

ciw.seed(0)
sim = ciw.Simulation(network)
sim.simulate_until_max_time(100)
records = sim.get_all_records()
print(len(records))
