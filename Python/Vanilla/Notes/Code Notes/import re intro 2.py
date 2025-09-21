import re

email = input("What's your email? ").strip()#.lower() can be used to handle cases or can use re.IGNORECASE

if re.search(r"^\w+@\w+.edu$", email, re.IGNORECASE ): #can do (\w|\s) \s = also allows space and whitespace
# \w means word , literally same like [a-zA-Z0-9_] almost
# THIS IS DOABLE if re.search(r"^\w+@\w.(edu|com|gov|net)$", email):
    print("Valid")
else:
    print("Invalid")



### NEW IDEAS
email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE ): #(\w+\.)? means after the ideas got grouped , it can show up once or not at all cuz of ? 
    print("Valid") # BEST FORM?
else:
    print("Invalid")
    
"""
\d = decimat digit
\D = not a decimal digit
\s = whitespace character
\S = not a whitespace character
\w = word character as well as numbers and underscores
\W = not a word character
A | B = either A or B
(...) =  a group
(?:...) = non-capturing version
re.IGNORECASE
re.MULTILINE
re.DOTALL
"""

