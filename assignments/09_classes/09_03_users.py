''''''
# Ciani Mason
# 6/10 difficulty

class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


user1 = User("Sarai", "Smith", 18, "New York", "sarai@email.com")
user2 = User("James", "Brown", 21, "California", "james@email.com")
user3 = User("Ciani", "Davis", 25, "Texas", "ciani@email.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user3.greet_user()