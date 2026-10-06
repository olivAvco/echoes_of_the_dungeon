import chars
import random

class Enemy(chars.Character):
    def __init__(self, name, eClass, max_hp, hp, attack, defense, level, xp_reward, gold_reward):
        super().__init__(name, eClass, max_hp, hp, attack, defense, level)
        self.eClass = eClass
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.is_protected = False
        self.protect_count = 0

    def loot_drop():
        return "You dropped an item!"

    def attack_target(self, target):
            target.take_damage(self.attack)

    def take_damage(self, damage):
        if self.is_protected:
            self.is_protected = False
            return

        damage_taken = max(1, damage - self.defense)
        self.hp -= damage_taken

        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
            return self.hp > 0

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

class Goblin(Enemy):
    def __init__(self):

        gold_chance = random.randint(1,10)
        if gold_chance == 10:
            self.gold_reward = 1
        else:
            self.gold_reward = 0

        super().__init__("Goblin","Goblin",18, 18, 7, 2, 1,10,gold_chance)  

        