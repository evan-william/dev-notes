with open("names.csv") as ANYTHING:
    for _ in ANYTHING:
        row = _.rstrip().split(",")
        # or name, gender = _.rstrip().split(",")
        # print(f"{name} is {gender}")
        print(f"{row[0]} is in {row[1]}")
        
        
        
print("\n")

# THIS BELOW IS FOR SORTING
students = []
    
with open("names.csv") as ANYTHING:
    for _ in ANYTHING:
        row = _.rstrip().split(",")
        students.append(f"{row[0]} is {row[1]}")
        
for _ in sorted(students):
     print(_)
     
    
print("\n")
    
# THIS FOR IDK
students = [] # LIST
    
with open("names.csv") as ANYTHING:
    for _ in ANYTHING:
        name, gender = _.rstrip().split(",")
        student = {} # DICT
        student["name"] = name
        student["gender"] = gender
        students.append(student)
        
for student in students:
    print(f"{student['name']} is in {student['gender']}")
     
    
print("\n")


#THIS IS SIMPLER THAN ABOVE
students = [] # LIST
    
with open("names.csv") as ANYTHING:
    for _ in ANYTHING:
        name, gender = _.rstrip().split(",")
        student = {"name" = name , "gender" = gender} # DICT
        students.append(student)
        
for student in students:
    print(f"{student['name']} is in {student['gender']}")
     
