import re

# Manual
"""
name = input("What's your name? ").strip()
if "," in name:
    Last, First = name.split(", ?") # This to fix if people use LastName, FirstName
    name = f"{First} {Last}" 
    print(f"Hello, {name}")
"""

# Library Usage
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name) # USING () can also to group them and capturing
if matches: # IF FOUND ","
    last, first = matches.groups() #.groups() to get back all the groups -> ()
    name = f"{first} {last}"
print(f"hello, {name}")


# TO GET WITHOUT matches.groups()
"""
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name) # USING () can also to group them and capturing
if matches: # IF FOUND ","  AND ALSO adding "?" or "*"  will fix "William,Evan" 
    last = matches.group(1) # NO NEED TO START FROM 0 ONLY WITH THIS LIBRARY
    first = matches.groups(2) 
    name = f"{first} {last}"
print(f"hello, {name}")
"""

# WALRUS OPERATION
"""
Can turn =>
matches = re.search(r"^(.+), (.+)$", name) # USING () can also to group them and capturing
if matches: # IF FOUND ","
    last, first = matches.groups() #.groups() to get back all the groups -> ()
    name = f"{first} {last}"
    
To =>
if matches := re.search(r"^(.+), (.+)$", name) # THIS IS WALRUS! , USED IF WANT TO ASSIGN SOMETHING AND ASK IF QUESTION
    last, first = matches.groups() 
    name = f"{first} {last}"

"""