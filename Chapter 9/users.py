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

user_01 = User("peter", "parker")
user_01.describe_user()
user_01.greet_user()

user_02 = User("owen", "wilson")
user_02.describe_user()
user_02.greet_user()

user_03 = User("josh", "smith")
user_03.describe_user()
user_03.greet_user()
