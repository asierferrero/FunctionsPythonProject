from eguneanBehin import eb
aukera=1
while aukera != 4:
    print("GAMES")
    print("---------------------------------")
    print("1.- Egunean behin")
    print("2.- Scisors-Paper-Stone")
    print("3.- Hangman")
    print("4.- I don´t want to play any more.")
    print()
    aukera = int(input("What game do you want to play? "))
    match aukera:
        case 1:
            name = input("What is your name? ")
            eb(name)
        case other:
            print("that option does not exist.")