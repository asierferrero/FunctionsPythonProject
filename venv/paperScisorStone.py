import random

def sps(name):
    p1hand=0;
    pcScore = 0;
    p1Score = 0;
    match = 0;

    while match < 5:
        answer = "incorrect"
        while answer == "incorrect":
            p1hand = int(input("what are you going to play? 0=Scisor, 1=stone, 2=paper "))
            match p1hand:
                case 0:
                    print("you showed Scisors")
                    answer = "correct"
                case 1:
                    print("you showed Scisors")
                    answer = "correct"
                case 2:
                    print("you showed Scisors")
                    answer = "correct"
                case other:
                    print("that option does not exist, try again")
        play = (random.randrange(3))
        match play:
            case 0:
                pchand = 0
                print("I showed Scisors")
                print("* *")
                print("  * *        * *")
                print("    * *    *     *")
                print("      * * *  * *")
                print("      * * *  * *")
                print("    * *    *     *")
                print("  * *        * *")
                print("* *")
                match=match+1
            case 1:
                pchand = 1
                print("I showed Stone")
                print("     * *")
                print("   * * * *  ")
                print("* * * * * * *")
                print("* * * * * * *")
                print("   * * * *  ")
                print("     * *")
                match = match + 1
            case 2:
                pchand = 2
                print("I showed Paper")
                print("* * * * * * *")
                print("*           *")
                print("*           *")
                print("*           *")
                print("*           *")
                print("*           *")
                print("* * * * * * *")
                match = match + 1
        if pchand == p1hand:
            print("It´s a draw")
        elif (p1hand == 0 and pchand == 2):
            print("you win! Well done " + name)
            p1Score = p1Score + 1
        elif (p1hand == 1 and pchand == 0):
            print("you win! Well done " + name)
            p1Score = p1Score + 1
        elif(p1hand == 2 and pchand == 1):
            print("you win! Well done " + name)
            p1Score = p1Score + 1
        elif (pchand == 0 and p1hand == 2):
            print("I win! " + name + ", you lost!! LOL")
            pcScore = pcScore + 1
        elif (pchand == 1 and p1hand == 0):
            print("I win! " + name + ", you lost!! LOL")
            pcScore = pcScore + 1
        elif (pchand == 2 and p1hand == 1):
            print("I win! " + name + ", you lost!! LOL")
            pcScore = pcScore + 1

    print("the final score is: " + name + " - ", p1Score, ", PC - " , pcScore)
    if pcScore == p1Score:
        print("It´s a draw")
    elif pcScore < p1Score:
        print("you win! Well done "+ name)
    elif pcScore > p1Score:
        print("I win! "+ name + ", you lost!! LOL")

