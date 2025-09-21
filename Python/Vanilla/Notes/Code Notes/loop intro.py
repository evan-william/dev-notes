# While
i = 3

while i != 0:
    print("meow")
    i -= 1
    
# For
for _ in [0, 1, 2]: # _ used becaue the variable there is useless
    print("woof")
    
for _ in range(3): 
    print("bark")
    
print("roar\n" * 3, end="")

while True:
    number = int(input("How many? "))
    if number < 0:
        print("Please enter a positive number!")
        continue
    else:
        break
    
for _ in range(number):
    print("meow")
    
    
# With Def
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True():
        n = int(input("What's n? "))
        if n < 0:
            print("Please enter a valid number!")
        else:
            print("Break")
    return n
        
def meow(n):
    for _ in range(n):
        ...
        
