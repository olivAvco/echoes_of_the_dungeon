import chars
import battle
import enemy

def start_game():

    print("Hello, adventure! Welcome to the world of Echoes of the Dungeon.")
    name = input("What is your name?: ")
    
    print(f"Pleasure to meet you, {name}!")
    print("Classes:\n- Warrior\n- Rogue\n- Paladin\n- Mage")
    
    while True:
        createClass = input("What is your class?: ").capitalize()
        if createClass not in ("Warrior","Paladin","Mage","Rogue"):
            print("Please choose a valid Class.")
        else:
            if createClass == "Warrior":
                Player = chars.Warrior(name)
                break
            elif createClass == "Paladin":
                Player = chars.Paladin(name)
                break
            elif createClass == "Rogue":
                Player = chars.Rogue(name)
                break
            else:
                Player = chars.Mage(name)
                break
    print(f"Ooh, a {createClass}!!")

    
    # tutorialGoblin = enemy.Goblin()
    # battle.Battle(Player,tutorialGoblin)