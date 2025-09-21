names = []

with open("names.txt") as file:
    for _ in file:
        names.append(_.rstrip())
        
for _ in sorted(names): # for _ in sorted(names, reserve=True): THIS CAN DO REVERSE ALPHABETICAL ORDER
    print(f"hello, {_}")
    
"""
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
"""

# THIS ABOVE WORKS SAME BUT MORE COMPACT


    