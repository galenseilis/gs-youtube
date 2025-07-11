import ciw
import matplotlib.pyplot as plt
import numpy as np


class TimeDepDist(ciw.dists.Distribution):
    def sample(self, t=0, ind=None):
        return np.sin(t) ** 2 + 1


dist = TimeDepDist()

time = np.linspace(0, 24, num=10_000)
samples = [dist.sample(t=t) for t in time]
plt.plot(time, samples)
plt.show()
