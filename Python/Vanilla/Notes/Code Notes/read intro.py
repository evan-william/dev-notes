with open("names.txt", "r") as ANYTHING: # r = read
    lines = ANYTHING.readlines() # lines = is just a variable can be anything , file.readlines() is to read all the line in names.txt
    
for _ in lines:
    print("hello,", _.rstrip()) # THIS TO STRIP THE NEXT LINE , CAN ALSO USE end=""
    
