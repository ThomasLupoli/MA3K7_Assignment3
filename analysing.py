import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import expon, gamma, weibull_min, lognorm
import math

oddcount = 0

Data = np.load("game_results.npy")

mean = np.mean(Data)
mode = stats.mode(Data)

print(mode)
print(f"mean = {mean}")




