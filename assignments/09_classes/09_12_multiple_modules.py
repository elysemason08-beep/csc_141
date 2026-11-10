#CIANI MASON
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        from user import User

class Privileges:
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
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

        from admin import Admin

admin = Admin("Ciani", "Mason")

admin.privileges.show_privileges() 