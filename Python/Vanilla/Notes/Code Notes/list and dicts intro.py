students = ["Kevin", "Laura", "Timothy"] # List

# print(students[2]) CAN DO THIS TO CHOOSE LIST!

for students in students:
   print(students)  # To print list
    
# Usage of Len (Len is to see how long a list is like range)
for i in range(len(students)):
    print(students[i])
    
# Dictionary
students2 = {
    "Kevin": "male", # Kevin = Key , male = Value
    "Laura": "female",
    "TImothy": "male",
}

print(students2["Kevin"]) # Will print the value of
                          # the chosen key
for student in students2:
    print(student) # Will only print the keys
    
for student in students2: 
    print(student, students2[student],sep=", ") # Will print all
    
students3 = [
    {"name": "Kevin", "gender": "male", "number": "1391"},
    {"name": "Jeff", "gender": "male", "number": "1031"},
    {"name": "Budi", "gender": "male", "number": "1739"},
    {"name": "Satria", "gender": "male", "number": "1001"},
    {"name": "Lingga", "gender": "male", "number": "1920"}  
]

for student in students3:
    print(student["name"], student["gender"], student["number"], sep =", ")

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "New Horizons": 58,
    "Pioneer 11": 44
}


def main2():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")
  #  for name in distances.keys(): #.valuues() also exist
  #     print(f"{name} is {distances[name]} AU from earth!")
  
def convert(au):
    return au * 149597870700

main2()

s = "CS50"

print(s[1:3])  # Output: "S5"  (Characters at index 1 and 2)
print(s[:3])   # Output: "CS5" (Starts from 0 by default, stops at index 2)
print(s[2:])   # Output: "50"  (Starts from index 2 and goes to the end)
print(s[:])    # Output: "CS50" (Copies the entire string)
print(s[-3:-1])  # Output: "S5" (Uses negative indexing)
print(s[-3:])  # Output: "S50" (Extracts last three characters)


s = "CS50"

print(s[0:4:2])  # Output: "C5"  (Takes every second character: index 0, 2)
print(s[::-1])   # Output: "05SC" (Reverses the string)
# s[::-1] reverses the string because it starts from the end (-1 step moves backwards).
 
def check_item(data, fruit): #THE USAGE OF CHECKING IF ITEMS IN DICTIONARY
    if fruit in data:
        print("Nutrition: ", end="")
        print(fruitdict[fruit])
    else:
        print("",end="")

fruitdict = {
        "apple": "130", # Key = Apple , Value = 130
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine" :"50",
        "watermelon": "80",
    }

fruit = input("Item: ").lower().strip()
check_item(fruitdict, fruit)

# UPDATING LIST/DICT 
def main():
    list = {}

    while True:
        try:
            addlist = input("Enter item: ").strip()
            if addlist in list:
                list[addlist] += 1
            else:
                list[addlist] = 1
                
        except EOFError:
            print()
            print("List: ")
            for _ , count in list.items():
                print(f"{_}: {count}")
            break
            
main()
    
# SORTING FUNCTION 
        except EOFError:
            print()
            for item in sorted(dict.keys()):  # Sorting keys alphabetically
                print(f"{dict[item]} {item}")
            break


    