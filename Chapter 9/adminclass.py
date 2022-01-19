"""Represents Admin and privileges"""

from userclass import User

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
