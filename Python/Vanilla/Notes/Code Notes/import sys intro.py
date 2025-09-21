import sys

print("hello, my name is", sys.argv[1]) # argv = argument vector

# it starts at [1] because [0] is the name of the program
# IF ERROR CAUSE THE USER DOESN'T WRITE for ex: python name.py David , WE CAN DO THIS =

try:
    print("hello, my name is", sys.argv[1])
except:
    print("Too few arguments")
    
# OR THIS
if len(sys.argv) < 2:
    print("Too few arguments")
elif len (sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
    
# PRINTING WITH python name.py "Evan William" , using quotations allows to print
# the thing fully

# THIS IS ALSO DO ABLE

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# THIS IS ALSO A FEATURE
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for name in sys.argv[1:]: # IF WE DONT USE [1:] IT WILL ALSO PRINT name.py (for example, my name is name.py)
    print("hello, my name is", arg)
    
for name in sys.argv[1:-1]:
    print("hello, my name is", arg) # THIS WILL ALSO ALLOW US TO CUTOUT LAST VALUE