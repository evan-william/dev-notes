# ==============================
# NUMPY & MATPLOTLIB: Histograms, Plots & Seed Demo
# ==============================

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# 1. Histogram Example
# --------------------------------
a = np.array([20, 87, 4, 40, 53, 74, 56, 51, 11, 20, 40, 15, 79, 25, 27])

# Fewer bins
plt.hist(a, bins=[0,20,40,60,80,100])
plt.title("Histogram (Bins: 0-20,20-40,...)")
plt.show()

# More bins
plt.hist(a, bins=list(range(0,101,10)))  # 0,10,20,...,100
plt.title("Histogram (Bins by 10s)")
plt.show()


# --------------------------------
# 2. Line Plot (Sine Graph)
# --------------------------------
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()


# --------------------------------
# 3. Random Numbers with SEED (Old vs New Style)
# --------------------------------

# --- Old Style ---
np.random.seed(50)  # sets global seed
a_old = np.array([1, np.random.randint(1, 10)])
print("Old style randint:", np.random.randint(1, 100))

plt.hist(a_old, bins=[0,20,40,60,80,100])
plt.title("Old Style RNG (np.random.seed)")
plt.show()

# --- New Style ---
rng = np.random.default_rng(50)  # independent generator
a_new = np.array([1, rng.integers(1, 10)])
print("New style randint:", rng.integers(1, 100))

plt.hist(a_new, bins=[0,20,40,60,80,100])
plt.title("New Style RNG (np.random.default_rng)")
plt.show()
