
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# Make a 6-sided die
six_sided_die = Die()

print("Rolling a 6-sided die:")
for roll in range(10):
    six_sided_die.roll_die()


# Make a 10-sided die
ten_sided_die = Die(10)

print("Rolling a 10-sided die:")
for roll in range(10):
    ten_sided_die.roll_die()


# Make a 20-sided die
twenty_sided_die = Die(20)

print("Rolling a 20-sided die:")
for roll in range(10):
    twenty_sided_die.roll_die()
