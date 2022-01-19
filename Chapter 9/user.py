"""Represent all type of users and their privileges including admin"""

class User:
    """Represent a user"""

    def __init__(self, first_name, last_name) -> str:
        self.first = first_name
        self.last = last_name
        self.fullname = f"{self.first} {self.last}"
        self.email = f"{self.first}.{self.last}@gmail.com"

    def describe_user(self) -> str:
        """Prints a summary of the user’s information"""

        print(f"\nUser's info:\n\tFirst name: {self.first.title()}\n\tLast name: {self.last.title()}\n\tEmail: {self.email}")

    def greet_user(self) -> str:
        """prints a personalized greeting to the user"""

        print(f"Hello {self.fullname.title()}\n")

class Privileges:
    """Represent a set of privileges"""

    def __init__(self, list = ["can add and delete post", "can allow special permission", "can ban user"]) -> list:
        self.privileges = list

    def show_privileges(self) -> str:
        """prints administrator’s set of privileges"""

        print(f"\nAdmin has privileges that {self.privileges}\n")

class Admin(User):
    """Represent an admin"""

    def __init__(self, first_name, last_name) -> str:
        super().__init__(first_name, last_name)
        self.privileges = Privileges(["can add and delete post", "can allow special permission", "can ban user"])
