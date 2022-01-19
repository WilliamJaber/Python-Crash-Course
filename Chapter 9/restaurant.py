"""Represent restaurant name, type and an open message"""

class Restaurant:

    def __init__(self, rest_name = str, cuisine_type = str) -> str:
        self.name = rest_name
        self.type = cuisine_type

    def describe_restaurant(self) -> str:
        """Prints the description of the restaurant: name and cuisine type"""

        print(f"\n{self.name.title()} is a restaurant that serves {self.type} food.\n")

    def open_restaurant(self) -> str:
        """Prints a message indicating that the restaurant is open"""

        print(f"{self.name.title()} is open at lunch and dinner time from Tuesday to Sunday.\n")
