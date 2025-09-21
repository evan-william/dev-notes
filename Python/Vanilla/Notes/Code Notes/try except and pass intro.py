try:
    x = int(input("What's x? "))
    print(f"x is {x}")
    
except ValueError: # If an error happends do below
    print("x is not an integer")
    

try:
    x = int(input("What's x? "))
    
except ValueError: # If an error happends do below
    print("x is not an integer")
    
print(f"x is {x}") # THIS WONT WORK EVENTHO WE DEFINED IT BEFORE AT LINE 10
# THIS HAPPENDS BECAUSE X SUPPOSED TO TAKE VALUE FROM RIGHT TO LEFT AND THUS
# AFTER IT RECIEVE VALUE IT BECOMES DEFINED, IN DETAIL:
# 1. Int(Input) recieve "cat" , it doesn't like it
# 2. Thus x is not defined even tho it's X = int(input) because int error
# 3. Thus line 3 will produce NameError: name 'x' is not defined

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
    
# THIS WILL DO TRY FIRST AND IF IT FOUND ERROR WILL EXECUTE EXCEPT CODE
# BUT IF FOUND NO ERROR IT WILL EXECUTE ELSE CODE

while True: # THIS A BETTER APPROACH 
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
    
    
while True: # ANOTHER WAY TOO
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


def main():
    x = get_int()
    print(f"x is {x}")
    
def get_int():
    while True: # ANOTHER WAY ASWELL WITH DEFINE USAGE BUT SHORTER
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x # DO KNOW THAT RETURN IS STRONGER THAN BREAK, NOT ONLY IT
                     # RETURNS THE VALUE BUT ALSO BREAK OUT OOF THE LOOP
def get_int():
    while True:
        try:
            return int(input("What's x? ")) # EVEN MORE COMPACT
        except ValueError:
            print("x is not an integer")

# THE USAGE OF PASS
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
        
main()

