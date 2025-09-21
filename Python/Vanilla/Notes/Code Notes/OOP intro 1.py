# TUPLE TO LIST
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name =  input("Name: ")
    house = input("House: ")
    return name, house # THIS IS A TUPLE (one value with 2 things inside)
    # KINDA LIKE LIST BUT ITS IMMUTABLE
    # SO print(f"student[0] from student[1]") ALSO WORKS
    # WHEN YOU WANNA CHANGE THE VALUE , IT WILL SAY TypeError: 'tuple' object bla bla bla

    # return [name, house]  THIS TURNS TUPLE TO LIST , BECOME MUTABLE

if __name__ == "__main__":
    main()
    
    
# TUPLE TO DICT
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {} # USAGE OF DICT MAKES IT MORE ACCURATE AND BETTER LIKE IF IT HAVE MORE THAN 2 FIELD
    student["name"] = input("Name: ")
    student["house"] = input("House: ") # DICT IS LIKE LIST , ALSO MUTABLE
    return student
    
    #name = input("Name: ")
    #house = input("House: ") THIS 3 LINES ALSO WORKS
    #return {"name": name, "house": house}\

if __name__ == "__main__":
    main()
    

