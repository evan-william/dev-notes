students = ["Hermione", "Harry", "Ron"]

""" WITHOUT ENUMERATE
for i in range(len(students)):
    print(i + 1, students[i])
"""

# With ENUMERATE
for i, student in enumerate(students):
    print(i + 1,student) # ENUMERATE TAKES A SEQUENCE OF VALUES AND GIVES BACK THE CURRENT INDEX
