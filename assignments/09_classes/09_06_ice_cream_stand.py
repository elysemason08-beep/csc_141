
"""
Ciani Mason
Exercise 9-6: Ice Cream Stand
"""

class Restaurant:
    """Model a Restaurant with OOP."""

    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}.')
        print(f'The cuisine type is {self.cuisine_type}.')
        print(f'The location is {self.location}.')
        print(f'The price range is {self.price_range}.')

    def can_you_take_a_date(self):
        if self.price_range <= 50:
            print(f"Don't embarrass yourself. It's too expensive {self.restaurant_name}.")
        else:
            print(f'Yes, this is in your price range {self.restaurant_name}.')


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        super().__init__(restaurant_name, cuisine_type, location, price_range)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'cookies and cream']

    def display_flavors(self):
        print("Available ice cream flavors:")

        for flavor in self.flavors:
            print(flavor)


# Create an instance of IceCreamStand.
ice_cream_stand = IceCreamStand(
    "Cici's Ice Cream",
    "Ice Cream",
    "Philadelphia",
    10
)

# Call the method.
ice_cream_stand.display_flavors()
