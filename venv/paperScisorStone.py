import random
p1hand=0;
pcScore = 0;
p1Score = 0;
match = 0;

while match < 5:
    play = (random.randrange(3))
    match play:
        case 0:
            pchand = 0
            print("I got Scisors")
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
            print("I got Stone")
            print("     * *")
            print("   * * * *  ")
            print("* * * * * * *")
            print("* * * * * * *")
            print("   * * * *  ")
            print("     * *")
            match = match + 1
        case 2:
            pchand = 2
            print("I got Paper")
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
    if (p1hand == 0 and pchand == 2) or (p1hand == 1 and pchand == 0) or (p1hand == 2 and pchand == 1):
        print("you win!")
    if (pchand == 0 and p1hand == 2) or (pchand == 1 and p1hand == 0) or (pchand == 2 and p1hand == 1):
        print("I win!")
