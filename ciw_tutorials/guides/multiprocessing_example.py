import ciw
import multiprocessing

MAX_TIME = 500
NUM_TRIALS = 200

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    number_of_servers=[3],
)


def get_mean_wait(network, seed=0, max_time=1000):
    ciw.seed(seed)
    sim = ciw.Simulation(network)
    sim.simulate_until_max_time(max_time)
    records = sim.get_all_records()
    waits = [record.waiting_time for record in records]
    avg_wait = sum(waits) / len(waits)
    return avg_wait


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=10)
    args = [(network, seed, MAX_TIME) for seed in range(NUM_TRIALS)]
    waits = pool.starmap(get_mean_wait, args)
    print(sum(waits) / NUM_TRIALS)
