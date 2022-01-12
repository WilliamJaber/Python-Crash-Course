def sandwiches(*ingredients) -> str:
    """Accepts a list of items a person wants on a sandwich and prints a summary"""

    print("\nYour sandwich is being prepared with the following ingredients:")
    for ingredient in ingredients:
        print(f">> {ingredient.title()}.")
    print()
#  Call the function three times, using a different number of arguments each time
sandwiches("parmesan cheese", "olives", "jam")
sandwiches("grilled peppers", "mushrooms")
sandwiches("caramelized onions")
