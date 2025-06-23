import ciw

network = ciw.create_network(
    arrival_distributions={
        'Baby': [
            ciw.dists.Exponential(rate=1.0),
            None,
            None,
        ],
        'Child': [
            ciw.dists.Exponential(rate=2.0),
            None,
            None,
        ],
    },
    service_distributions={
        'Baby': [
            ciw.dists.Exponential(rate=4.0),
            ciw.dists.Exponential(1.0),
            ciw.dists.Deterministic(value=0.0), # WARN: Not used.
        ],
        'Child': [
            ciw.dists.Exponential(rate=6.0),
            ciw.dists.Deterministic(value=0.0),
            ciw.dists.Exponential(rate=1.0),
        ],
    },
    routing={
        'Baby': [
                [0.0, 1.0, 0.0],
                [0.0] * 3,
                [0.0] * 3,
                 ],
        'Child': [
                    [0.0, 0.0, 1.0],
                    [0.0] * 3,
                    [0.0, 0.0, 0.0],
        ],
    },
    number_of_servers=[1, 2, 3],
)

NUM_TRIALS = 16

average_waits_1_babies = []
average_waits_1_children = []
average_waits_2 = []
average_waits_3 = []
for trial in range(NUM_TRIALS):
    ciw.seed(trial)
    sim = ciw.Simulation(network)
    sim.simulate_until_max_time(30)
    recs = sim.get_all_records()
    waits1_babies = [
        r.waiting_time
        for r in recs
        if r.node==1 and 
        r.arrival_date > 3 and 
        r.arrival_date < 27 and 
        r.customer_class == 'Baby'
    ]
    waits1_children = [
        r.waiting_time
        for r in recs 
        if r.node==1 and 
        r.arrival_date > 3 and 
        r.arrival_date < 27 and 
        r.customer_class == 'Child'
    ]
    waits2 = [
        r.waiting_time
        for r in recs
        if r.node==2 and 
        r.arrival_date > 3 and 
        r.arrival_date < 27
    ]
    waits3 = [
        r.waiting_time 
        for r in recs 
        if r.node==3 and 
        r.arrival_date > 3 
        and r.arrival_date < 27
    ]
    average_waits_1_babies.append(sum(waits1_babies) / len(waits1_babies))
    average_waits_1_children.append(sum(waits1_children) / len(waits1_children))
    average_waits_2.append(sum(waits2) / len(waits2))
    average_waits_3.append(sum(waits3) / len(waits3))

# visited_by_babies = {1, 2}
# assert set([r.node for r in recs if r.customer_class=='Baby']) == visited_by_babies
# visited_by_children = {1, 3}
# assert set([r.node for r in recs if r.customer_class=='Child']) == visited_by_children
#

print(sum(average_waits_1_babies) / len(average_waits_1_babies))
print(sum(average_waits_1_children) / len(average_waits_1_children))
print(sum(average_waits_2) / len(average_waits_2))
print(sum(average_waits_3) / len(average_waits_3))



















