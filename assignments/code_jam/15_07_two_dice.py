''''''
# ITS NOT RUNNING RIGHT
import plotly.express as px
from die import Die

# STEP 1: Create three standard six-sided dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# STEP 2: Store the combined results of each roll.
results = []

# STEP 3: Roll all three dice 1,000 times.
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# STEP 4: Find all possible totals: 3 through 18.
min_result = 3
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(min_result, max_result + 1)

# STEP 5: Count how often each total appears.
frequencies = []

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# STEP 6: Create a colorful visualization.
fig = px.bar(
    x=list(poss_results),
    y=frequencies,
    title="THREE DICE: The Triple Roll Challenge",
    labels={
        "x": "Total of Three Dice",
        "y": "Frequency"
    },
    template="plotly_dark",
    color=frequencies,
    color_continuous_scale="plasma"
)

# STEP 7: Polish the chart.
fig.update_layout(
    title_x=0.5,
    xaxis_dtick=1,
    showlegend=False
)

# STEP 8: Display the graph.
fig.show()
