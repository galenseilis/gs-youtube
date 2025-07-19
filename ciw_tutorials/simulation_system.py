import ciw
import random

NUM_NODES = 10
SEED = 2025

def generate_routing_matrix(N, seed=None):
    """
    Generates a routing matrix for use in the Ciw discrete event simulation library.

    Each row corresponds to a node in the network, and contains the probabilities
    of routing a customer from that node to every other node. All entries are 
    non-negative and each row sums to a value less than or equal to 1, allowing
    for the possibility of a customer exiting the system.

    Parameters:
        N (int): The number of nodes in the network.
        seed (int, optional): Random seed for reproducibility.

    Returns:
        list[list[float]]: An N x N routing matrix suitable for use in Ciw.
    """
    if seed is not None:
        random.seed(seed)

    routing_matrix = []
    for _ in range(N):
        # Generate N random positive values
        row = [random.random() for _ in range(N)]
        # Choose a target sum ≤ 1
        target_sum = random.random()  # In [0, 1]
        total = sum(row)
        # Normalize and scale
        scaled_row = [(x / total) * target_sum for x in row]
        routing_matrix.append(scaled_row)

    return routing_matrix

def generate_random_positive_integers(N, max_value=100, seed=None):
    """
    Generates a list of N random positive integers.

    Parameters:
        N (int): The number of integers to generate. Must be positive.
        max_value (int, optional): Maximum value for each integer (default 100).
        seed (int, optional): Random seed for reproducibility.

    Returns:
        list[int]: A list of N random positive integers.
    """
    if seed is not None:
        random.seed(seed)
    if N <= 0:
        raise ValueError("N must be a positive integer.")

    return [random.randint(1, max_value) for _ in range(N)]


def generate_random_non_negative_floats(N, max_value=100.0, seed=None):
    """
    Generates a list of N random non-negative floating-point numbers.

    Parameters:
        N (int): Number of floats to generate. Must be positive.
        max_value (float, optional): Maximum value for each float (default 100.0).
        seed (int, optional): Random seed for reproducibility.

    Returns:
        list[float]: A list of N random non-negative floats.
    """
    if seed is not None:
        random.seed(seed)
    if N <= 0:
        raise ValueError("N must be a positive integer.")

    return [random.uniform(0.0, max_value) for _ in range(N)]

def generate_exponential_random_vector(N, max_rate=100, seed=None):
    rates = generate_random_non_negative_floats(N, max_value=max_rate, seed=seed)
    return [ciw.dists.Exponential(rate) for rate in rates]

network = ciw.create_network(
    arrival_distributions=generate_exponential_random_vector(NUM_NODES, max_rate=10, seed=SEED),
    service_distributions=generate_exponential_random_vector(NUM_NODES, max_rate=200, seed=SEED),
    routing=generate_routing_matrix(NUM_NODES, seed=SEED),
    number_of_servers=generate_random_positive_integers(NUM_NODES, SEED),
)

ciw.seed(SEED)

Q = ciw.Simulation(network)
Q.simulate_until_max_time(100, progress_bar=True)
