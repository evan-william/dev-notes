import random
# from random import choice

# ^^^^ THIS VERSION WILL MAKE U ABLE TO DO
# coin = choice(["heads", "tailts"]) instead

# USAGE OF IMPORT RANDOM
coin = random.choice(["heads", "tails"]) # RANDOM CHOICE
print(coin)

number = random.randint(1, 20) # RANDOM INT
print(number)

cards = ["jack", "queen", "king"] # RANDOM SHUFFLE
random.shuffle(cards)
print(cards)

cards = ["jack", "queen", "king"]
for _ in cards:
    print(_)

