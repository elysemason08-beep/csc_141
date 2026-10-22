# Ciani Mason
# Difficulty level 2/10
# You walked us through this in class.
import matplotlib.pyplot as plt

cubes = [x**3 for x in range(1, 5001)]
fig, ax = plt.subplots()
ax.plot(cubes)
plt.show()
