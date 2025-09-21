email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
    
#### CAN ALSO DO THIS
"""
username, domain = email.split("@")

if (username) and ("." in domain):   # CHECK IF THERES ATLEAST USERNAME and IF . in DOMAIN 
    print("Valid")             # THIS IS SEPERATED , DOESNT MEAN IT ASK FOR USERNAME AND . IN DOMAIN
else:
    print("Invalid")
"""

### CAN ALSO BE MORE SPECIFIC
"""
if username and domain.endswith(".edu"): # THIS CHECKING IS MORE SPECIFIC
    print("Valid")
else:
    print("Invalid")
"""

# THIS WILL GET TIRING QUICKLY
    
