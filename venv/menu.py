from paperScisorStone import sps

aukera=1
while aukera != 4:
    print("GAMES")
    print("---------------------------------")
    print("1.- Egunean behin")
    print("2.- Scisors-Paper-Stone")
    print("3.- Hangman")
    print("4.- I don´t want to play any more.")
    print()
    aukera = input("What game do you want to play? ")
    match aukera:
        case 1:

        case 2:
            name = input("What is your name? ")
            sps(name)
        case 3:
            
        case 4:
            print("Goodbye, come again soon!")
        case other:
            print("that option does not exist.")