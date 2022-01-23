from random import choices

def lottery():
    """Randomly choose four values between numbers and letters for lottery"""

    valid_numbers = ["4", "8", "2", "6", "7", "5", "1", "3", "0", "9", "A", "B", "C", "D", "E"]
    winning_ticket = choices(valid_numbers, k=4)
    return winning_ticket

def Analysis():
    """Prints a message reporting how many times the loop had to run to give you the winning ticket"""

    my_ticket = lottery()
    print(f"Any ticket matching these four numbers or letters wins a prize: {my_ticket}")

    ctr = 0
    while True:
        lotto = lottery()

        if my_ticket == lotto:
            print(f'\nMatch!>>> {my_ticket} == {lotto}')
            break
        else:
            print(f'{my_ticket} {lotto} ==> No Match!!')
            ctr += 1

    print(f"It took {ctr} loops to match the winning lottery ticket!")

Analysis()
