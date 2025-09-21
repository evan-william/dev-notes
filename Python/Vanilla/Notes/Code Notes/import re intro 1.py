import re

email = input("What's your email? ").strip()

if re.search(r"^(.+)@(.+)\.edu$", email): # Without the "r" it will intrepert the "\" as something else
                        # "r" means to treat it as raw string
# THIS IS PRIMITIVE: if re.search(".+@.+", email): # CAN ALSO DO ..*@..*
# DO NOT DO THIS if re.search(".+@.+.edu", email):
# BUT DO THIS INSTEAD if re.search(".+@.+\.edu", email): this will want the last one to be .edu
# cause only using the .edu without \ will allow something like david@harvard?edu
    print("Valid")
else:
    print("Invalid")

# THIS IS POSSIBLE: if re.search(r"^[^@]+@[^@]+\.edu$", email)
# THIS IS ALSO POSSIBLE: if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.edu$", email) doesn't need to write abcde etc
# This means [^@]+ , any character except the "@" sign , then the + is like before (1 or more rep)
# so it can be like this:

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
    
"""
. = any character except a newline
* = 0 or more repetitions
+ = 1 or more repetitions
? = 0 or 1 repetitions
{m} = m repetitions
{m,n} = m-n repetitions
^ = matches the start of the string
$ = matches the end of the string or just before the newline at the end of the string
[] = set of characters
[^] = complementing the set
"""