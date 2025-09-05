from Enemy import Enemy


class Elf(Enemy):
    def __init__(self, name):
        super().__init__(name)

    def take_damage(self, damage):
        self.health -= damage
        print("How could you hit a baby?!")
