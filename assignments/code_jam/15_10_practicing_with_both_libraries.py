''''''
# IM SICK AND TIRED SEE YOU IN OFFICE HOURS TMR I HATE THAT I DONT UNDERSTAND THIS CHAPTER
# Ciani Mason

# im tired and sick
import matplotlib.pyplot as plt
from die import Die

# Create two six-sided dice.
die_1 = Die()
die_2 = Die()

# Roll both dice 1,000 times and store their sums.
results = []

for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# Find the possible sums and count their frequencies.
poss_results = range(2, 13)
frequencies = [results.count(value) for value in poss_results]

# Create a bar chart using Matplotlib.
fig, ax = plt.subplots()

ax.bar(poss_results, frequencies)

# Add labels and a title.
ax.set_title("Two Dice: Matplotlib Edition")
ax.set_xlabel("Combined Dice Total")
ax.set_ylabel("Frequency")
ax.set_xticks(list(poss_results))

# Display the chart.
plt.tight_layout()
plt.show()
