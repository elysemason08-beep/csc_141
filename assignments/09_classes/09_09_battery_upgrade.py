
# Ciani Mason

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print the range this battery provides."""

        if self.battery_size == 40:
            car_range = 150
        elif self.battery_size == 65:
            car_range = 225

        print(f"This car can go about {car_range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it isn't already 65 kWh."""

        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represent an electric car."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Create an electric car with the default battery.
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Display the range before upgrading.
my_leaf.battery.get_range()

# Upgrade the battery.
my_leaf.battery.upgrade_battery()

# Display the range after upgrading.
my_leaf.battery.get_range()
