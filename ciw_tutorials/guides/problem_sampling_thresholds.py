import ciw


class TimeDependentDist(ciw.dists.Distribution):
    def sample(self, t, ind=None):
        if t < 55:
            return 10
        if t < 58:
            return 0.1
        return 10


Pi = ciw.dists.PoissonIntervals(
    rates=[1, 8],
    endpoints=[3, 4],
    max_sample_date=10,
)

N = ciw.create_network(
    arrival_distributions=[Pi],
    service_distributions=[ciw.dists.Deterministic(value=0.0)],
    number_of_servers=[float("Inf")],
)

ciw.seed(0)
Q = ciw.Simulation(N)
Q.simulate_until_max_time(101)
recs = Q.get_all_records()
print([r.arrival_date for r in recs])
