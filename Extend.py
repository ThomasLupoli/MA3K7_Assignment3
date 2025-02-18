import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = range(1000, 18_001, 1000)
mean = [0.1779, 0.1697, 0.1644, 0.1603, 0.1573, 0.1563, 0.1522, 0.1479, 0.1526, 0.1527, 0.1504, 0.1468, 0.1519, 0.1463, 0.1487, 0.142, 0.144, 0.1487]

plt.plot(x, mean, "r-")
plt.xlabel("Pieces of Paper")
plt.ylabel("Mean / Pieces of Paper")
plt.title("How does the mean change?")
plt.show()


