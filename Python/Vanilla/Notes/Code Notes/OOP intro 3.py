class Student:
    def __init__(self, name, house):
       # VARIALBES CAN BE MADE OPTIONAL by doing (self, name, house=None) !!!!!
        if not name: # CHECK FOR ERROR CAN BE DONE IN CLASS TOO
            raise ValueError("Missing Name")
        if house not in ["Rungkud" , "Darjo" , "Ambon" , "Amba"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        
    def __str__(self): # THIS CALLED SELF, AND ONLY TAKES 1 ARGUMENT 
        return f"{self.name} from {self.house}" # THIS WILL BE PRINTED WHEN LINE 18 INITIATED
        # CAUSE PYTHON WILL AUTOMATICALLY CALL THIS FUNCTION WHEN STUFF ASK FOR ANY STR INPUT
        # BTW U CAN CREATE A NAME ERROR WITH CUSTOM NAME LIKE EvanError
      
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    # DOING print(student) will pop out a <__main__.Student object at 0x10blablabla

def get_student(): 
    name = input("Name: ")                       
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()
    

