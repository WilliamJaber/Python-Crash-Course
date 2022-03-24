from dataclasses import dataclass, field


@dataclass
class User:
    """Represent a user"""
    first_name: str
    last_name: str
    full_name: str = field(init=False)  # This field will not be required when you initialize this object
    email: str = field(init=False)      # This field will not be required when you initialize this object

    def __post_init__(self):
        """Because of this, you have to create email and full_name prior to initialization to handle the
        describe_user function below."""
        self.email = f'{self.first_name}.{self.last_name}@gmail.com'
        self.full_name = f'{self.first_name} {self.last_name}'

    def describe_user(self) -> None:
        """Prints a summary of the user’s information"""
        print(f"\nUser's info:\n\tFirst name: {self.first_name.title()}\n\tLast name: {self.last_name.title()}\n"
              f"\tEmail: {self.email}")

    def greet_user(self) -> None:
        """prints a personalized greeting to the user"""
        print(f"Hello {self.full_name.title()}\n")


if __name__ == '__main__':
    user_01 = User("peter", "parker")
    user_01.describe_user()
    user_01.greet_user()

    user_02 = User("owen", "wilson")
    user_02.describe_user()
    user_02.greet_user()

    user_03 = User("josh", "smith")
    user_03.describe_user()
    user_03.greet_user()
