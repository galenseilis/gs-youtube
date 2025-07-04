import ciw

network = ciw.create_network(
    arrival_distributions={
        'Class 0': [
            ciw.dists.Deterministic(value=0.4),
            ciw.dists.Empirical(observations=[0.1, 0.1, 0.1, 0.2]),
        ],
        'Class 1': [
            ciw.dists.Deterministic(value=0.2),
            ciw.dists.Pmf(values=[0.2, 0.4], probs=[0.5, 0.5]),
        ]
    },
    service_distributions={
        'Class 0': [
            ciw.dists.Exponential(rate=6.0),
            ciw.dists.Lognormal(mean=1, sd=0.5),
        ],
        'Class 1': [
            ciw.dists.Uniform(lower=0.1, upper=0.7),
            ciw.dists.Triangular(lower=0.2, mode=0.3, upper=0.7),
        ],
    },
    routing={'Class 0': [[0.0, 0.0], [0.0, 0.0]],
    'Class 1': [[0.0, 0.0], [0.0, 0.0]],},
    number_of_servers=[1, 1],
)


ciw.seed(10)
sim = ciw.Simulation(network, exact=10)
sim.simulate_until_max_time(50)
records = sim.get_all_records()
