from random import *

try:    
    guess = randint(0,10)
    computer1 = randint(0,10)
    GuessList = []
    GuessList.append(computer1)

    while computer1 != guess:
        computer1 = randint(0,100)
        if computer1 not in GuessList:
           GuessList.append(computer1)
           print("COmputer guessed ",computer1)
            
   

    ''' 
    while (computer1 not in GuessList) and (computer1 != guess):
        computer1 = randint(0,5)
        GuessList.append(computer1)
        print("COmputer guessed ",computer1)

    '''
    '''
    while computer1 != guess:
        #computer1 = random.choice(GuessesLeft)
        print("COmputer guessed ",computer1)
        while computer1 in GuessList:
            computer1 = randint(0, 5)
            #GuessList.append(computer1)
        computer1 = randint(0,5)        
'''
except KeyboardInterrupt:
    print("goodbye")
    

print("COMPUTER FINALLY GUESSED " , guess)
for c in GuessList:
   print(c)
    



