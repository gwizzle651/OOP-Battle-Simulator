import random
from Enemy import Enemy


class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name, luck=20)
        self.maxHealth = 500
        self.strength = 25

    def attack(self):
        baseDamage = random.randint(1, self.strength)
        critical = random.randint(0, 100) < self.luck
        if critical:
            baseDamage *= 2
        return baseDamage

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage."
              "Health is now {self.health}.")
        if self.remainingHealth < self.maxHealth * 0.25:
            print(f"{self.name} is enraged! Attack power increased!")
            self.strength += 10
