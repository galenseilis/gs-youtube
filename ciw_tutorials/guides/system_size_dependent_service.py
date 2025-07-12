import ciw

class StateDependentDist(ciw.dists.Distribution):
    def sample(self, t=None, ind=None):
        n = ind.simulation.statetracker.state
        return max((-0.05 * n) + 0.2, 0)

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=4)],
    service_distributions=[StateDependentDist()],
    number_of_servers=[1],
)

if __name__ == "__main__":
    ciw.seed(0)
    simulation = ciw.Simulation(network, tracker=ciw.trackers.SystemPopulation())
    simulation.simulate_until_max_time(500)
    records = simulation.get_all_records()
    services = [record.service_time for record in records if record.arrival_date > 100]
    average_queue_size = sum(
        s * p for s, p in simulation.statetracker.state_probabilities().items()
    )
    print("Average Observed service time: ", sum(services) / len(services))
    print(
        "Theoretical Average at Observed Queue size: ",
        (-0.05 * average_queue_size) + 0.2,
    )
