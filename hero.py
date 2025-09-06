import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.maxHealth = 1200
        self.remainingHealth = self.maxHealth
        self.strength = random.randint(10, 30)
        self.healingPower = 30

    def strike(self):
        return random.randint(1, self.strength)

    def receive_damage(self, damage):
        self.remainingHealth -= damage
        if self.remainingHealth < 0:
            self.remainingHealth = 0

    def heal(self):
        self.remainingHealth += self.healingPower
        if self.remainingHealth > self.maxHealth:
            self.remainingHealth = self.maxHealth

    def is_alive(self):
        return self.remainingHealth > 0
