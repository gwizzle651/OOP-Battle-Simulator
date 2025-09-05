import random


class Hero:
    """
    This is our hero blueprint.

    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """

    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.strength = random.randint(1, 100)
        self.healingPower = 30

    def strike(self):
        return random.randint(1, self.strength)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def special_ability(self):
        self.health += self.healingPower

    def is_alive(self):
        return self.health > 0
