from random import choices

def lottery():
    """Randomly choose four values between numbers and letters for lottery"""

    valid_numbers = ["4", "8", "2", "6", "7", "5", "1", "3", "0", "9", "A", "B", "C", "D", "E"]
    winning_ticket = choices(valid_numbers, k=4)
    print(f"\nAny ticket matching this sequence of four numbers and letters wins a prize.\n{winning_ticket}\n")

lottery()
