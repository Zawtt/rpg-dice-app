import random

class Dice:
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self, quantity: int = 1, modifier: int = 0):
        results = [random.randint(1, self.sides) for _ in range(quantity)]
        total = sum(results) + modifier
        return results, total
