import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import expon, gamma, geom
import math
from scipy.stats import chisquare


Data = np.load("game_results_10million.npy")

data = ((Data + 1) / 2)

prob = np.zeros(1013)

for i in range(10_000_000):
    prob[math.ceil(Data[i] / 2) - 1] += 1

prob = prob/10_000_000
p_est = 1 / np.mean(data)
xx = np.arange(1013) + 1
pmf_geom = geom.pmf(xx, p_est)

expected_counts = pmf_geom * np.sum(prob)

expected_counts *= np.sum(prob) / np.sum(expected_counts)

plt.hist(data, bins=40, edgecolor="black", density=True, alpha=0.6, label="Histogram")
plt.plot(xx, prob, 'g-', label="Probability from Sample")
plt.plot(xx, pmf_geom, 'm-', label="Geometric")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.title("Histogram with Geometric Fit")
plt.show()

chi2_stat, p_value = chisquare(prob, expected_counts)

print("Chi-Square Statistic:", chi2_stat)
print("P-value:", p_value)
