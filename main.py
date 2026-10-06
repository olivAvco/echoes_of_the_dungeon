import functions

while True:

    print("--Echoes of the Dungeon--")
    print("1. New Game")
    print("2. Exit")

    command = input("What do you want to do?: ")
    if command == "1":
        print("Let's start a new game!")
        functions.start_game()
        exit()

    elif command == "2":
        print("Cya.")
        exit() 
