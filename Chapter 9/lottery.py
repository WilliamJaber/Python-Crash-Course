from random import choice

def main():
    """Randomly choose between numbers and letters for lottery"""

    valid_numbers = [4, 8, 2, 6, 7, 5, 1, 3, 0, 9, "A", "B", "C", "D", "E"]
    winning_ticket = []

    n = 0
    while n < 4:
        n += 1
        result = winning_ticket.append(choice(valid_numbers))
    print(f"\nAny ticket matching these sequence of numbers and letters wins a prize.\n{winning_ticket}\n")

main()
