from hangman import *
print("Jokoak")
print("---------------------------------")
print("1.- Egunean behin")
print("2.- Harri-Horri-Har")
print("3.- Hangman")
print("4.- Ez dut gahiago jolastu nahi.")
print()
aukera = int(input("zertan jokatu nahi duzu? "))
match aukera:
    case 1:
        print("Asier")
    case 2:
        print("Asier")
    case 3:
        print("Asier")
    case 4:
        print("Goodbye, come again soon!")
    case other:
        print("That option does not exist.")