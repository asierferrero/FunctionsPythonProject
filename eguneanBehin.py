import time

a = "1"
while not (a == "0"):

    score = 0
    start_time = time.time()  #start the time

    print("EGUNEAN BEHIN")
    print("===========================================================================================")
    print("1. ? ")

    print("a) ")
    print("b) ")
    print("c) ")

    x = input("Answer a, b or c: ")

    if x == "a":
        score = score + 1

    print("===========================================================================================")

    print("2. ? ")

    print("a) ")
    print("b) ")
    print("c) ")

    x = input("Answer a, b or c: ")

    if x == "b":
        score = score + 1

    print("===========================================================================================")

    print("3. ")

    print("a) ")
    print("b) ")
    print("c) ")

    x = input("Answer a, b or c: ")

    if x == "c":
        score = score + 1

    print("===========================================================================================")

    end_time = time.time()  #stop the time

    print("Your score is " + str(score) + "/10 and you did it in " + str(end_time - start_time) + " seconds")

    a = input("Do you want to play again? ")

    if a == "yes":
        a = 1

    elif a == "no":
        a = 0

    else:
        print("You have to enter 'yes' or 'no'")




