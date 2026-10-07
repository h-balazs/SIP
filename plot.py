import numpy as np
import matplotlib.pyplot as plt


value, count = np.loadtxt(
    "Histogram_of_clown.csv",
    delimiter=",",
    skiprows=1,
    dtype=float,
    unpack=True)

plt.plot(value, count)

plt.savefig("Histogram.png", dpi=300)
