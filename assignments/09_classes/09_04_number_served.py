
"""
Ciani Mason
Exercise 9-4: Number Served
"""

class Restaurant:
    """Model a Restaurant with OOP."""

    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range
        self.number_served = 0

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

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, customers):
        self.number_served += customers


# Create an instance of the Restaurant class.
restaurant = Restaurant("Cici Shack", "Soul Food", "Philadelphia", 50)

# Print the default number of customers served.
print(f"Customers served: {restaurant.number_served}")

# Change the number served and print it again.
restaurant.number_served = 25
print(f"Customers served: {restaurant.number_served}")

# Use the set_number_served() method.
restaurant.set_number_served(100)
print(f"Customers served: {restaurant.number_served}")

# Use the increment_number_served() method.
restaurant.increment_number_served(50)
print(f"Customers served: {restaurant.number_served}")
