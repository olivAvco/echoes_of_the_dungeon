

class Character:
    def __init__(self, name, pClass, max_hp, hp, attack, defense, level):
        self.name = name
        self.pClass = pClass
        self.max_hp = max_hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.level = level

        self.is_protected = False
        self.protect_count = 0

    def take_damage(self, damage):
        if self.is_protected:
            self.is_protected = False
            return

        damage_taken = max(1, damage - self.defense)
        self.hp -= damage_taken

        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0

    def attack_target(self, target):
        target.take_damage(self.attack)

    def protect(self):
        if self.protect_count == 0:
            chance = 1.0
        else:
            chance = 0.5 ** self.protect_count

        import random
        if random.random() < chance:
            self.is_protected = True
            self.protect_count += 1
            return True

        self.protect_count = 0
        return False
        


class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name=name,
            pClass="Warrior",
            max_hp=10,
            hp=10,
            attack=10,
            defense=4,
            level=1
        )

        self.stamina = 6 #ver dps

    def power_strike(self, target): #ver dps
        self.stamina -= 4

        if self.stamina > 0:
            bonus_damage = 5
            damage = self.attack + bonus_damage
            target.take_damage(damage)
        else:
            print("You can't use Power Strike now! You don't have enough stamina.")
    def level_up(self):
        self.level += 1

        self.max_hp += 2
        self.hp += 2
        self.attack += 2
        self.defense += 1
        self.stamina += 1 #ver dps

class Rogue(Character):
    def __init__(self, name):
        super().__init__(
            name=name,
            pClass="Rogue",
            max_hp=13,
            hp=13,
            attack=9,
            defense=1,
            level=1
        )

        self.concentration = 10 #ver dps

    def level_up(self):
        self.level += 1

        self.max_hp += 1
        self.hp += 1
        self.attack += 1
        self.defense += 1
        self.concentration += 1 #ver dps

class Paladin(Character):
    def __init__(self, name):
        super().__init__(
            name=name,
            pClass="Paladin",
            max_hp=10,
            hp=10,
            attack=10,
            defense=3,
            level=1
        )

        self.holy_power = 10 #ver dps

    def level_up(self):
        self.level += 1

        self.max_hp += 1
        self.hp += 1
        self.attack += 1
        self.defense += 1
        self.holy_power += 1 #ver dps

class Mage(Character):
    def __init__(self, name):
        super().__init__(
            name=name,
            pClass="Mage",
            max_hp=6,
            hp=6,
            attack=12,
            defense=2,
            level=1
        )

        self.mana = 10

    def level_up(self):
        self.level += 1

        self.max_hp += 1
        self.hp += 1
        self.attack += 8
        self.defense += 1
        self.mana += 1 #ver dps