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
        if self.remainingHealth < 0:
            self.remainingHealth = 0
        print(f"{self.name} takes {damage} damage.\n"
              f"Health is now {self.remainingHealth}.")

    def is_alive(self):
        return self.remainingHealth > 0
