import ciw
import matplotlib.pyplot as plt

N = 10_000

dist1 = ciw.dists.Exponential(10)
samples1 = [dist1.sample() for _ in range(N)]

dist2 = ciw.dists.Gamma(1, 2)
samples2 = [dist2.sample() for _ in range(N)]

dist3 = dist1 + dist2
samples3 = [dist3.sample() for _ in range(N)]

dist1 - dist2
dist1 * dist2
dist1 / dist2
