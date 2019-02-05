
from random import *
import time

try:

    start_time = time.time()
    
    #guess = int(input("Guess a number 1 to 20: "))#randint(0,100000)
    guess = randint(0,100)
    computer1 = randint(0,100)
    computer2 = 0
    count = 0
    GuessList = [ ]
    GuessList.append(computer1)
    
    while computer1 != guess:
        computer1 = randint(0,100)
        #human = int(input("Guess a number 1 to 20: "))   
        if computer1 not in GuessList:
            GuessList.append(computer1)
            print("COmputer guessed ",computer1)
            computer2 += computer1   
            count += 1
            computer1 /= 2
            print(computer1)
            round(computer1)
            print("ff ",computer1)
            if computer1 not in GuessList:
                GuessList.append(computer1)
                print("COmputer guessed ",computer1)



except KeyboardInterrupt:
    print("goodbye")
    

print("!!!!!!COMPUTER FINALLY GUESSED " , guess)
print("went through loop ", count, " times.")
print("Computer total: ", computer2)
print("--- %s seconds ---" % (time.time() - start_time))

