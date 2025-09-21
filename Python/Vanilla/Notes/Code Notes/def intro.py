# Basic Function
def hello():
    print(f"Hello, {name}")
    
name = input("What's your name? ")
hello()

# Extra
def hello(x):
    print("Hello,", x)
    
name = input("What's your name? ")
hello(name)
    
# Play With Parameters
def hello(x = "World"):
    print("Hello,", x)

hello()

name = input("What's your name? ")
hello(name)

# Def Order
def main():
    name = input("What's your name? ")
    hello(name)
    
def hello(x ="world"):
    print("hello,", x)
    
main()

# THIS WONT WORK
def main():
    name = input("What's your name? ")
    hello()
    
def hello():
    print("hello,", name)
    
main()


# ADDITIONAL
def main():
    x = int(input("What's X?"))
    print("X Squared is", square(x))

def square(n):
    return n * n #Can do n ** 2 or pow(n,2)

"""
n will return value to square(x)
"""

main()


# WITH RETURN
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$",""))



def percent_to_float(p):
    return float(p.replace("%","")) / 100


main()


