import random


class Enemy:
    def __init__(self, name, luck):
        self.name = name
        self.maxHealth = 100
        self.remainingHealth = self.maxHealth
        self.luck = luck
        self.strength = random.randint(5, 15)

    def attack(self):
        return random.randint(1, self.strength)

    def take_damage(self, damage):
        self.remainingHealth -= damage
        print(f"{self.name} takes {damage} damage."
              "Health is now {self.health}.")

    def is_alive(self):
        return self.remainingHealth > 0
