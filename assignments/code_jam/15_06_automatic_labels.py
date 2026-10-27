''''''
# Ciani Mason
#

frequencies = []
poss_results = range(1, die.num_sides + 1)

''''''
#
import plotly.express as px
from assignments.code_jam.die import Die

die_1 = Die(8)
die_2 = Die(8)
results = []


for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


frequencies = []

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


title = "Results of Rolling Two D8 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(
    x=poss_results,
    y=frequencies,
    title=title,
    labels=labels
)

fig.update_layout(xaxis_dtick=1)
fig.show()

import matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

plt.show()
