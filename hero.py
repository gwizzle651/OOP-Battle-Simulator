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
        self.maxHealth = 1000
        self.remainingHealth = self.maxHealth
        self.strength = random.randint(1, 100)
        self.healingPower = 30

    def strike(self):
        return random.randint(1, self.strength)

    def receive_damage(self, damage):
        self.remainingHealth -= damage
        if self.remainingHealth < 0:
            self.remainingHealth = 0

    def special_ability(self):
        self.remainingHealth += self.healingPower
        if self.remainingHealth > self.maxHealth:
            self.remainingHealth = self.maxHealth

    def is_alive(self):
        return self.health > 0
