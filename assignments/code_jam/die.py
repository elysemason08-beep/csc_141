''''''


from random import randint

class Die:
    """A reusable die that can have any number of sides."""

    def __init__(self, num_sides=6):
        # Store how many sides this die has.
        self.num_sides = num_sides

    def roll(self):
        # Return one random number from 1 through the number of sides.
        return randint(1, self.num_sides)
