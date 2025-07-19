import ciw

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=100),
                           ciw.dists.Exponential(rate=1)],
    service_distributions=[ciw.dists.Exponential(rate=1),
                           ciw.dists.Exponential(rate=1)],
    routing=[[0.0, 0.5],
             [0.0, 0.0]],
    number_of_servers=[3, 2],
    system_capacity=100,
)

ciw.seed(0)
Q = ciw.Simulation(N, tracker=ciw.trackers.SystemPopulation())
Q.simulate_until_max_time(1000)
state_probs = Q.statetracker.state_probabilities()
print(state_probs)
