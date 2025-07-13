import ciw

# Define a simple 2-node network
N = ciw.create_network(
    arrival_distributions=[
        [ciw.dists.Exponential(1.0)],  # Arrivals at Node 1
        [None]                         # No external arrivals at Node 2
    ],
    service_distributions=[
        [ciw.dists.Exponential(2.0)],  # Service at Node 1
        [ciw.dists.Exponential(2.0)]   # Service at Node 2
    ],
    routing=[[0.0, 1.0], [0.0, 0.0]],  # Routing: Node 1 -> Node 2
    number_of_servers=[1, 1],
    queue_capacities=[2, 1]  # Node 1 has capacity 2, Node 2 has capacity 1
)

recs = Q.get_all_records(only=['rejection'])
dr = recs[0]
dr
