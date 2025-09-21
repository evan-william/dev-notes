def main():
    yell("This", "is" ,"CS50")

def yell(*words):
    uppercased = [word.upper() for word in words] # LIST COMPREHENSION
    print(*uppercased)
    
main()

"""
students = [
    {"name": "Budi", "house": "Rungkud"},
    {"name": "Jeni", "house": "Sunter"},
    {"name": "Roni", "house": "Gresik"},
    {"name": "Dracon", "house": "Slytherin"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]): #s: will sort based on name
    print(gryffindor["name"])
"""