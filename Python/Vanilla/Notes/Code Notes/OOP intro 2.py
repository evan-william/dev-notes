class Student: # CLASS IS NEW DATA TYPE (CAN SAY THAT ITS A BLUEPRINT)
    def __init__(self, name, house):        
       self.name = name
       self.house = house
       # THE OBJECT CREATED FROM THE CLASS IS both MUTABLE OR IMMUTABLE
       # CLASS CAN COME WITH ALOT OF METHODS OR FUNCTION
       # def __init__ is what function that will always be called like from line 23
       # THE NAME def __init__ is like that from the author, to initialize an object
       
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():  # TO GET VALUE FROM A CLASS LIKE BEFORE
    student = Student() # AFTER DEFINING CLASS , CAN USE THE student. notation to store attributes
    # THIS LINE ABOVE IS LIKE USING the STUDENT() blue print to create a house called student
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

    """ # THIS ALSO WORKS                     Student() class is like function kinda
    name = input("Name: ")                       ^
    house = input("House: ")                     |
    student = Student(name, house) # THIS CALLED THE CLASS AND FILLS THE VARIABLE
    return student
    
    btw can also do for line 24-25 to become:
    return Student(name, house)
    """

if __name__ == "__main__":
    main()
    
### FOR BETTER EXPLANATION OF INIT AND CLASS ###
"""
1. self is a third variable (other than name and house) that has to come first
2. self gives access to the current object that we have created for ex. line 24
3. Then we populate it with values
"""
