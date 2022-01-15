class User:
    """Represent a user"""

    def __init__(self, first_name, last_name) -> str:
        self.first = first_name
        self.last = last_name
        self.fullname = f"{self.first} {self.last}"
        self.email = f"{self.first}.{self.last}@gmail.com"
        self.login_attempts = 0

    def describe_user(self) -> str:
        """Prints a summary of the user’s information"""

        print(f"\nUser's info:\n\tFirst name: {self.first.title()}\n\tLast name: {self.last.title()}\n\tEmail: {self.email}")

    def greet_user(self) -> str:
        """prints a personalized greeting to the user"""

        print(f"Hello {self.fullname.title()}\n")

    def increment_login_attempts(self) -> int:
        """Increments the value of login_attempts by 1"""

        self.login_attempts += 1

    def reset_login_attempts(self) -> int:
        """Resets the value of login_attempts to 0"""

        self.login_attempts = 0

user = User("peter", "parker")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"You attempt {user.login_attempts} logins.")

user.reset_login_attempts()
print(f"Your login attempts is been reset to {user.login_attempts}.")
