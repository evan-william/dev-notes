import random
import sys

try:
    level = int(input("Level: "))
    cnumber = random.randint(1,level)
except ValueError:
    sys.exit("Only enter number!")
        
while True:
    guess = input("Guess: ")
    
    if guess.isdigit():
        if int(guess) > cnumber:
            print("Too large!")
        elif int(guess) < cnumber:
            print("Too few!")
        else:
            print("Just right!")
            break 
    else:
        pass
        
        
        