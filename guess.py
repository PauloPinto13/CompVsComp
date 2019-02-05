
from random import *
import time
def main():
    try:


        start_time = time.time()
        computer1Max = int(input("Input a max(the larger the number the longer it takes): "))
        #guess = int(input("Guess a number 1 to 20: "))#randint(0,100000)
        guess = randint(0,computer1Max)
        computer1 = randint(0,computer1Max)
        computer2 = 0
        count = 0
        GuessList = [ ]

        GuessList.append(computer1)
        GuessTuple = tuple(GuessList)
        while computer1 != guess:
            computer1 = randint(0,computer1Max)
            #human = int(input("Guess a number 1 to 20: "))   
            if computer1 not in GuessTuple:
                GuessList = list(GuessTuple)
                GuessList.append(computer1)
                GuessTuple = tuple(GuessList)
                print("COmputer guessed ",computer1)
                computer2 += computer1   
                count += 1
            


    except KeyboardInterrupt:
        print("goodbye")
    

    print("COMPUTER FINALLY GUESSED " , guess)
    print("went through loop ", count, " times.")
    print("Computer total: ", computer2)
    print("--- %s seconds ---" % (time.time() - start_time))

    '''for c in GuessList:
           print(c)
    '''

main()
