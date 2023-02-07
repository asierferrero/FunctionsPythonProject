import time

a = 1
while a == 1:

    score = 0 #initial score
    fail = 0
    start_time = time.time()  #start the time

    print("EGUNEAN BEHIN")
    print("===========================================================================================")

    name = input("Enter your name before starting: ")
    print("===========================================================================================")

    print(name + ", get ready!")

    duration = 3  # duration of the timer
    x = 0

    while x < duration:
        remaining_time = duration - int(x)
        x += 1  # equivalent to x++
        print(str(remaining_time))
        time.sleep(1)

    print("===========================================================================================")

    print("1. What is the output of the following code: print('Hello, World!'[1:5])")

    print("a) World")
    print("b) ell")
    print("c) ello")

    x = input("Answer a, b or c: ")

    if x == "b":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("2. What is the result of the following code: x = 'hello'; y = 'world'; print(x + y)? ")

    print("a) worldhello")
    print("b) hello world")
    print("c) helloworld")

    x = input("Answer a, b or c: ")

    if x == "c":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("3. What does the following code do: for i in range(10): print(i)")

    print("a) Prints the numbers 0 through 9")
    print("b) Prints the numbers 1 through 10")
    print("c) Prints the numbers 10 through 1")

    x = input("Answer a, b or c: ")

    if x == "a":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("4. What is the purpose of the following code: def hello(): print('Hello, World!')? ")

    print("a) Prints 'Hello, World!' once.")
    print("b) Prints 'Hello, World!' ten times.")
    print("c) Prints 'Hello, World!' whenever the code is run.")

    x = input("Answer a, b or c: ")

    if x == "a":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("5. What is the result of the following code: x = 5; y = 10; print(x + y)? ")

    print("a) 10")
    print("b) 15")
    print("c) 5")

    x = input("Answer a, b or c: ")

    if x == "b":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("6. What is the purpose of the 'if' statement here: if x > y: print('x is greater than y')? ")

    print("a) To check if x is greater than y")
    print("b) To check if x is less than or equal to y")
    print("c) To check if x is equal to y")

    x = input("Answer a, b or c: ")

    if x == "a":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("7. What is the result of the following code: x = [1, 2, 3, 4, 5]; print(len(x))? ")

    print("a) 4")
    print("b) 5")
    print("c) 6")

    x = input("Answer a, b or c: ")

    if x == "b":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("8. What is the purpose of the following code: x = [1, 2, 3, 4, 5]; y = x[2:4]? ")

    print("a) To create a new list y with elements 2 through 4 of the list x")
    print("b) To create a new list y with elements 1 through 4 of the list x")
    print("c) To create a new list y with elements 3 through 5 of the list x")

    x = input("Answer a, b or c: ")

    if x == "a":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("9. What is the output of the following code: x = {'name': 'John', 'age': 30} print(x['name'])? ")

    print("a) 30")
    print("b) John")
    print("c) name")

    x = input("Answer a, b or c: ")

    if x == "b":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    print("10. What is the purpose of the 'import' statement in the following code: import math? ")

    print("a) To include the math module in the code")
    print("b) To exclude the math module from the code")
    print("c) To replace the math module with a new one")

    x = input("Answer a, b or c: ")

    if x == "a":
        score = score + 1

    else:
        fail = fail + 1

    print("===========================================================================================")

    end_time = time.time()  #stop the time

    total_time = end_time - start_time #total time without rounding
    final_time = round(total_time, 2) #round the decimals of the final time

    print(name + ", you scored " + str(score) + "/10 and you did it in " + str(final_time) + " seconds")

    a = input("Do you want to play again? (yes/no): ")

    if a == "yes":
        a = 1

    elif a == "no":
        a = 0
        print("Goodbye!")

    else:
        print("You have to enter 'yes' or 'no'")
