x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
    
# Usage of "or"
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
# Usage of "and"
score = int(input("Score: "))

if score <= 100 and score >= 80: # 100>= score >= 80 
    grade = "A";
    print(f"Your grade is {grade}!")
elif score < 80 and score >= 60: # 80> score >= 60
    grade = "B";
    print(f"Your grade is {grade}!")
elif score < 60 and score >= 0: # 60> score >= 0
    grade = "Failed";
    print(f"You {grade}!")
    
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    
def is_even(n): 
    if n % 2 == 0:  #CAN COMPACT THIS INTO [return True if n % 2 == 0 else False]
        return True
    else:
        return False
"""  
BOOLEAN ARGUMENT LIKE n % 2 == 0 already have True
or False Value so might as well just do :

def is_even(n):
    return n % 2 == 0  #THIS IS THE MOST SIMPLE MODEL
"""

main()

name = input("")

# USEAGE OF MATCH CASE
match name:
    case "Budi": #CAN DO "Budi" | "Adi" | "Haris":
        print("Indonesia")
    case "Adi":
        print("Indonesia")
    case "Haris":
        print("Indonesia")
    case _:
        print("Not Indonesia")

# ANOTHER USAGE OF IF WITH DEF
def main():
    greeting= input("Greeting= ").strip().lower()
    print(f"${startexe(greeting)}")

def startexe(greeting):
    if greeting.startswith("h"):
        return 20
    elif greeting.startswith("hello"):
        return 0
    else:
        return 100

main()
