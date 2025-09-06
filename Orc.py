import random
from Enemy import Enemy


class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name, luck=15)
        self.maxHealth = 500
        self.strength = 20

    def attack(self):
        whichAttack = random.choice(["smash", "slash", "stomp"])
        print(f"{self.name} uses {whichAttack}!")
        if whichAttack == "smash":
            damage = random.randint(10, self.strength + 10)
            self.remainingHealth -= 15
            print(f"\n{self.name} hurts itself while smashing!\n"
                  f"Health is now {self.remainingHealth}.")
        elif whichAttack == "slash":
            damage = random.randint(5, self.strength)
        elif whichAttack == "stomp":
            damage = random.randint(1, self.strength - 5)
            strengthReduction = random.randint(1, 3)
            print(f"\n{self.name} stomps your hero to the ground,"
                  " reducing your hero's strength!")
        damage = random.randint(1, self.strength)
        critical = random.randint(0, 100) < self.luck
        if critical:
            damage *= 2
            print(f"Critical hit by {self.name}!")
        return damage, strengthReduction if whichAttack == "stomp" else 0

    def take_damage(self, damage):
        self.remainingHealth -= damage
        if self.remainingHealth < 0:
            self.remainingHealth = 0
        print(f"{self.name} takes {damage} damage. "
              f"Health is now {self.remainingHealth}.")
        if self.remainingHealth < self.maxHealth * 0.25:
            print(f"{self.name} is enraged! Attack power increased!")
            self.strength += 10
