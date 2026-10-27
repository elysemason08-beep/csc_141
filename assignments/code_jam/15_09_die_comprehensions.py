''''''
# ITS NOT RUNNING RIGHT IM ANGRY
import plotly.express as px
from random import randint

results = [randint(1, 6) + randint(1, 6) + randint(1, 6)
           for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(3, 19)]

title = "Results of Rolling Three D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency'}
fig = px.bar(x=range(3, 19), y=frequencies, title=title,
             labels=labels)

fig.show()