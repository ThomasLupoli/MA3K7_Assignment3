import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

Data = np.load("game_results.npy")
Data = np.random.choice(Data, size=10_000, replace=False)
data = np.sort((Data + 1) / 2)
p_est = 1 / np.mean(data)

theoretical_quantiles = stats.geom.ppf(np.linspace(0.01, 0.99, len(data)), p_est)
print(theoretical_quantiles)

plt.scatter(theoretical_quantiles, data, alpha=0.6, label="Observed vs. Geometric")
plt.plot(theoretical_quantiles, theoretical_quantiles, 'r--', label="Perfect Fit")

plt.xlabel("Geometric Quantiles")
plt.ylabel("Sample Quantiles")
plt.legend()
plt.title("QQ Plot")
plt.grid()
plt.show()
