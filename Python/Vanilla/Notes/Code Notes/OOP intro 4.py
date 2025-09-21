class Student: # CAN ALSO CREATE OUR OWN DEF insaide
    def __init__(self, name, house, patronus):
        if not name: 
            raise ValueError("Missing Name")
        if house not in ["Rungkud" , "Darjo" , "Ambon" , "Amba"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} from {self.house} with {self.patronus}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "HORSEEMOJI"
            case "Otter":
                return "OTTEREMOJI"
            case "Jack Russel Terrier":
                return "DogEMOJI"
            case _: # WILL POP UP IF USER JUST PRESS ENTER
                return "/"
              
def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student(): 
    name = input("Name: ")                       
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
    


