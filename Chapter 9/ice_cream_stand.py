# parent class
class Restaurant:
    """Represent different restaurants name, type and an open message"""

    def __init__(self, rest_name = str, cuisine_type = str) -> str:
        self.name = rest_name
        self.type = cuisine_type

    def describe_restaurant(self) -> str:
        """Prints the description of the restaurant: name and cuisine type"""

        print(f"\n{self.name.title()} is a restaurant that serves {self.type} food.\n")

    def open_restaurant(self) -> str:
        """Prints a message indicating that the restaurant is open"""

        print(f"{self.name.title()} is open at lunch and dinner time from Tuesday to Sunday.\n")

# child class
class IceCreamStand(Restaurant):
    """Represent different restaurants name, type and an open message"""

    def __init__(self, rest_name = str, cuisine_type = str) -> str:
        """Initialize attributes of the parent class"""

        super().__init__(rest_name, cuisine_type)
        self.flavors = ["strawberry", "chocolate", "vanilla", "ice sandwich"]

    def get_flavors(self) -> str:
        """displays these flavors"""

        print(f"We have a variety of flavors such as:\n{self.flavors}.\n")


ice_cream = IceCreamStand("Ice Cream Stand", "frozen", )
ice_cream.describe_restaurant()
ice_cream.get_flavors()
