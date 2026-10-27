''''''
# BRO 
# ciani mason

import plotly.express as px
from random import randint

results = []

for roll_num in range(1000):
    result = randint(1, 6) * randint(1, 6)
    results.append(result)

frequencies = [results.count(value) for value in range(1, 37)]

title = "Results of Multiplying Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency'}

fig = px.bar(x=range(1, 37), y=frequencies, title=title,
             labels=labels)

fig.show()