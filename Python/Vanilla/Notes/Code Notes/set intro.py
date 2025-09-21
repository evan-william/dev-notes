# To filter out duplicate
students = [
    {"name": "John", "house": "Dawg"},
    {"name": "John1", "house": "Dawg1"},
    {"name": "John2", "house": "Dawg2"},
    {"name": "John3", "house": "Dawg3"},
    {"name": "John4", "house": "Dawg4"},
]

houses = set() # Can use this instead of house = []
for student in students:
    houses.add(student["house"]) # Use .add and not .append for set()
    # WIll automaticly remove duplicate
    
for house in sorted(houses): # Sort the strings alphabeticly
    print(house)
    

