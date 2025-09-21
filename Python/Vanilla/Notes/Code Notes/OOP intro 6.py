import random

class Hat:
    """ THIS IS NO LONGER NEEDED IF HAVE THE BELOW!
    def __init__(self):
        self.houses = ["A", "B", "C"]
    """
    houses = ["A", "B", "C"]
    
    @classmethod # WONT WORK WITH CLS IF NO @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)
        
""" THIS IS USED ONLY IF USE SELF AND NOT CLS
hat = Hat() # To instanciate an object of a certain class
"""
#hat.sort("Harry") NO LONGER DO THIS IF USE CLS BUT CAN DO THIS BELOW!
Hat.sort("Harry")
    