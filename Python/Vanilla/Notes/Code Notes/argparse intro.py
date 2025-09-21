import sys
import argparse

# USAGE OF SYS
""" 
if len(sys.argv) == 1: # THIS USER ONLY TYPE THE NAME OF THE PROGRAM
    print("Hello")
elif len(sys.argv) == 3 and sys.argv[-1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: Found.py")
"""

# USAGE OF ARGPARSE   # "Desccription and help is literally what it does
parser = argparse.ArgumentParser(description="Meow like a cat") # "parser =" can be anything 
parser.add_argument("-n", default=1, help ="number of times to meow", type=int) 
args = parser.parse_args() # WILL AUTOMATICALY TO IMPORT SYS and LOOK SYS.ARGV
           # Default is literally what it does and type give it a hint on what type of data it is
# for _ in range(int(args.n)):
for _ in range(args.n):
    print("meow")
    
# WHEN HIT RUN WITHOUT ARGV THE DEFAULT VALUE IS SET TO 1 SO IT "MEOWS" 1 TIME
# LINE 22 Sargs.n contain the interger that human type after after a space after -n    
