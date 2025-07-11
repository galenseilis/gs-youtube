import ciw
import matplotlib.pyplot as plt

comp1 = ciw.dists.Gamma(1, 2)
comp2 = ciw.dists.Gamma(10, 2)


dist = ciw.dists.MixtureDistribution(
    [
        comp1,
        comp2,
    ],
    [0.75, 0.25],
)

samples1 = [comp1.sample() for _ in range(10_000)]
samples2 = [comp2.sample() for _ in range(10_000)]
samples = [dist.sample() for _ in range(10_000)]
plt.hist(samples, bins=100, label="mixture")
plt.hist(samples1, bins=100, label="comp1", alpha=0.25)
plt.hist(samples2, bins=100, label="comp2", alpha=0.25)
plt.legend()
plt.show()
