''''''
# ITS NOT RUNNING RIGHT
#ciani mason 

import plotly.express as px
from die import Die

# STEP 1: Create two six-sided dice.
die_1 = Die()
die_2 = Die()

# STEP 2: Prepare a list for the products.
results = []

# STEP 3: Roll both dice 1,000 times and MULTIPLY the values.
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# STEP 4: List every possible product from 1 through 36.
poss_results = range(1, 37)

# STEP 5: Count the frequency of each possible product.
frequencies = []

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# STEP 6: Build the visualization.
fig = px.bar(
    x=list(poss_results),
    y=frequencies,
    title="DICE MULTIPLICATION: Beyond Addition",
    labels={
        "x": "Product of Both Dice",
        "y": "Frequency"
    },
    template="plotly_dark",
    color=frequencies,
    color_continuous_scale="turbo"
)

# STEP 7: Improve the chart layout.
fig.update_layout(
    title_x=0.5,
    xaxis_dtick=1,
    showlegend=False
)

# STEP 8: Display the visualization.
fig.show()
