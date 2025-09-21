# try mypy (FILENAME).py to find type error like this

"""
def cat(n: int) -> None: # This will hardcode it to return none
    for _ in range(n):     (CAN CHANGE TO str, int, etc)
        print("meow") 
     
     
number: int = input("Number: ") 
meow(number)
"""

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

def cat(n: int): # the ": int" is to give hint to mypy it's an int so that program wont error
    for _ in range(n): # program error in the first place cause the line 6 takes the
        print("meow") # input of str but line 2 ask for int cuz its using in range()
     
     
number: int = input("Number: ") # Same like number 6
meow(number)