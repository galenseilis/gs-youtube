import ciw
import pandas as pd

SELECTED_COLUMNS = ["id_number", "arrival_date", "waiting_time"]


network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=1)],
    service_distributions=[ciw.dists.Exponential(rate=2)],
    number_of_servers=[1],
)

ciw.seed(0)
sim = ciw.Simulation(network)
sim.simulate_until_max_time(5)
records = pd.DataFrame(sim.get_all_records())
print(records[SELECTED_COLUMNS])

sim.simulate_until_max_time(9)
records = pd.DataFrame(sim.get_all_records())
print(records[SELECTED_COLUMNS])
