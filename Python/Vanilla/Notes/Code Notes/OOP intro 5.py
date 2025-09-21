class Student: # CAN ALSO CREATE OUR OWN DEF insaide
    def __init__(self, name, house):
         """  THIS ERROR CHECK IS NO LONGER NEEDED IF HAVE GETTER SETTER 
        if not name: 
            raise ValueError("Missing Name")
        if house not in ["Rungkud" , "Darjo" , "Ambon" , "Amba"]:
            raise ValueError("Invalid House")
        """
        self.name = name
        self.house = house # WHY this not use _house too? check cs50 week 8 1:36:36
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name): 
        if not name:
            raise ValueError("Missing Name")
        self._name = name
        
        
    @property# GETTER = GETS SOME ATRIBUTE
    def house(self):
        return self._house
     # BOTH THE NAME IS DESIGNED THIS WAY
    @house.setter # SETTER = SETS SOME VALUE , BOTH GET SET THIS TO FIX 33 (LIKE ERROR CHECKING)
    def house(self, house):
        if house not in ["Rungkud" , "Darjo" , "Ambon" , "Amba"]:
            raise ValueError("Invalid House")
        self._house = house # "_" is so that the python doesnt get confuse cuz theres variable house and thres function house
    
""" GET SET MUMBO JUMBO
1) When stuff like line 33 happends , python wont allow user to just directly access
   student.house (AKA Self.house)
2) It will instead call the setter cuz it see at line 33 at the left hand side, if there is self.house
   and its the name of the getter or setter , and it sees an equal sign "=" , it will
   not let the code access that attribute directly , but will use the setter instead
3) Setter will always get called when there is .house?
"""

def main():
    student = get_student()
    student.house = "Nigga"
    print(student)

def get_student(): 
    name = input("Name: ")                       
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
    



