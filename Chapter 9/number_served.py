class Restaurant:
    """Represent different restaurants name, type and an open message"""

    def __init__(self, rest_name = str, cuisine_type = str) -> str:
        self.name = rest_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self) -> str:
        """Prints the description of the restaurant: name and cuisine type"""

        print(f"{self.name.title()} is a restaurant that serves {self.type} food.\n")

    def open_restaurant(self) -> str:
        """Prints a message indicating that the restaurant is open"""

        print(f"{self.name.title()} is open at lunch and dinner time from Tuesday to Sunday.\n")

    def set_number_served(self, num_customers) -> int:
        """sets the number of customers that have been served"""

        self.number_served = num_customers

    def increment_number_served(self, num_customers) -> int:
        """increment and prints the number of customers that have been served"""

        self.number_served += num_customers
        print(f"Today we served {self.number_served} customers!")

restaurant = Restaurant("bonhomia", "fusion")
print(restaurant.number_served)

restaurant.number_served = 20
print(restaurant.number_served)

restaurant.set_number_served(50)
print(restaurant.number_served)

restaurant.increment_number_served(25)
