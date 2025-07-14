import ciw

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=2),
                           ciw.dists.Exponential(rate=1)],
    service_distributions=[ciw.dists.Exponential(rate=1),
                           ciw.dists.Exponential(rate=1)],
    routing=[[0.0, 0.5],
             [0.0, 0.0]],
    number_of_servers=[3, 2],
    queue_capacities=[float('inf'), 10]
)

if __name__ == "__main__":
    ciw.seed(0)
    Q = ciw.Simulation(N)
    Q.simulate_until_max_time(100)
    recs = Q.get_all_records(only='service')
    dr = recs[381]
    print(dr)
