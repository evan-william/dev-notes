""" BASIC UNPACKING
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first} ")
"""

# Better Unpacking
# def total (galleons=0, sickles=0, knuts=0) THIS CAN BE DONE IF WANT TO UNPACK LESS THAN 3 VALUE , IT SETS DEFAULT VALUE TO 0
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts") OLD SCHOOL WAY
print (total(*coins), "Knuts") # BETTER WAY , "*" will unpack the list of 3
# print (total(**coins), "Knuts") CAN USE THIS, DOUBLE "**" TO UNPACK DICT BELOW
# "**" ALSO IS LIKE UNPACKING TO (galleons=100, sickles=50, knuts=25)

""" ANOTHER OLD SCHOOL WITH DICT
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
    
coins = {"galleons": 100, "sickles":50, "knuts": 25}

print (total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts") 
"""


""" THIS ALSO UNPACK LIST
def main():
    yell(["This", "is" ,"CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased) # THIS WILL UNPACK LIST TOO
    
main()
"""