from math import sqrt
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
Max = 0
Min = 0
Mode = 0
for i in range(len(value)):
    if count[i] != 0:
        Max = i
    if count[len(value)-1-i] != 0:
        Min = len(value)-1-i
    if count[i] > count[Mode]:
        Mode = i
StdDev = sqrt(np.sum((count*(value-Mean)**2))/N)


plt.text(50, 2000, f"N={N}     Mean={Mean}",
    bbox=dict(facecolor="white", alpha=0.5, boxstyle="square"))
plt.text(50, 1860, f"Max={Max}       Min={Min}",
    bbox=dict(facecolor="white", alpha=0.5, boxstyle="square"))
plt.text(50, 1720, f"Mode={Mode}         StdDev={StdDev}",
    bbox=dict(facecolor="white", alpha=0.5, boxstyle="square"))


plt.bar(value, count, width=1, align="edge")
plt.title("Histogram of the 'clown' sample image")
plt.xlabel("pixle colour [as 8-bit value]")
plt.ylabel("pixle count")



plt.savefig("Histogram.png", dpi=300)
plt.show()
