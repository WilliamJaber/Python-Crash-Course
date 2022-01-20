from random import randint

class Die:
    """Sets a die sides and roll it"""

    def __init__(self, sides = 6) -> int:
        self.sides = sides

    def roll_die(self) -> int:
        """Prints a random number between 1 and the number of sides the die has"""

        random_num = randint(1, self.sides)
        print(random_num)

die_1 = Die()
die_2 = Die(sides = 10)
die_3 = Die(sides = 20)

n = 0
while n < 10:
    n += 1
    die_1.roll_die()
print()

n = 0
while n < 10:
    n += 1
    die_2.roll_die()
print()

n = 0
while n < 10:
    n += 1
    die_3.roll_die()
print()
