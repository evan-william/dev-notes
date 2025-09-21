class Wizard:
    def __init__(self, name): # CAN ALSO DO (self, name, patronus)
        if not name:
            raise ValueError("Missing Name")
        self.name = name

class Student(Wizard): # THIS (Wizard) is called inheritance which will inherit characteristic of class wizard
    def __init__(self, name, house):
        super().__init__(name) # Super is to access the super class 
        self.house = house
        
    ...
    
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
