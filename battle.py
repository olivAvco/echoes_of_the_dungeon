class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

        
        print(
            "== BATTLE ==\n"
            f"Player: {self.player.name}\n"
            f"Class: {self.player.pClass}\n"
            f"HP: {self.player.hp}\n\n"
            f"Enemy: {self.enemy.name}\n"
            f"Class: {self.enemy.eClass}\n"
            f"HP: {self.enemy.hp}\n\n"
            f"1. Attack\n"
            f"2. Protect\n"
            f"3. Potion\n"
            f"4. Run\n"
        )



        import random
        enemyMovies = [self.enemy.attack_target(), self.enemy.protect]

        whoMoves = random.randint(1,10)
        if whoMoves >= 5:
            enemyCommand = random.choice(enemyMovies)
        
        battleCommand = input("What do you want to do?: ")