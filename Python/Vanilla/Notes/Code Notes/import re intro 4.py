import re
"""
url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
"""
# THIS WAY HAVE SO MANY PROBLEM

# USE PREFIX BUT SUCK ANYWAY
"""
url = input("URL: ").strip()
username = url.removeprefix("https://twitter.com/", "") # 
print(f"Username: {username}")
""" # THIS ABSOLUTELY DOES NOTHING BTW


# USAGE OF re
url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# FOR http https can do (http|https) and fine to add ? to make it optional
# For ? mean it makes the s optional
# For (www\.)? means it will tolerate www being there or not CAN ALSO DO (www\.|) 
print(f"Username: {username}")


# Usage of search again if user type random bs like google.com
"""
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) #(.+) to capture it
if matches:
    print(f"Username: ", matches.group(2)) => cuz (1) is www eventho it only meant to group them not capture
    
    
SO WE CAN DO =>
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE) #(.+) to capture it
if matches:
    print(f"Username: ", matches.group(1))
    
    [[Usage at ?:www so it doesnt capture it]]
"""

# FORMAT of RE.SUB
"""
re.sub(pattern, repl, string, coount=0, flags= 0)
"""
