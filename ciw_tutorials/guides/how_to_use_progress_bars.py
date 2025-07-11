import ciw
from tqdm import tqdm

NUM_TRIALS = 100

network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(10)],
    service_distributions=[ciw.dists.Exponential(20)],
    number_of_servers=[1],
)

for trial in tqdm(range(NUM_TRIALS)):
    ciw.seed(trial)
    sim = ciw.Simulation(network)
    sim.simulate_until_max_customers(100)
    records = sim.get_all_records()
