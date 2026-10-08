import numpy as np
import matplotlib.pyplot as plt


value, count = np.loadtxt(
    "Histogram_of_clown.csv",
    delimiter=",",
    skiprows=1,
    dtype=float,
    unpack=True)

N = np.sum(count)
Mean = np.sum(value*count)/N



plt.bar(value, count, width=1, align="edge")
plt.title("Histogram of the 'clown' sample image")
plt.xlabel("pixle colour [as 8-bit value]")
plt.ylabel("pixle count")



plt.savefig("Histogram.png", dpi=300)
plt.show()
