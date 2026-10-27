''''''
# Ciani Mason
# Difficulty level 2/10

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Create a random walk with 5,000 steps.
rw = RandomWalk(5_000)
rw.fill_walk()

# Plot the random walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Show the plot.
plt.show()
