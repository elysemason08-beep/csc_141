
# Ciani Mason

class User:
    """Represent a user."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Privileges:
    """Store an administrator's privileges."""

    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """Represent an administrator."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


# Create an Admin instance.
admin = Admin("Ciani", "Mason")

# Show the administrator's privileges.
admin.privileges.show_privileges()
