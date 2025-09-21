import re

# FIRST EXTRA
def main():
    code = input("Hexadecimal color code: ")
    pattern = r"^#[a-fA-F0-9]{6}$" # WLL EXPECT 6 CHARACTER
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")
    
main()

# SECOND EXTRA
locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main2():
    pattern2 = r"(?P<countrycode>\+\d{1,3}) \d{3}-\d{3}-\d{4}" #?P<> is used to name a capture group
    number = input("Number: ")
    
    match2 = re.search(pattern2, number)
    if match2:
        countryCode = match2.group("countrycode") # CAPTURE d{1,3}
        print("Valid")
        print(locations[countryCode])
    else:
        print("Invalid")
    
main2()
