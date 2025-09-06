from Enemy import Enemy
import random


class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, luck=random.randint(1, 10))
