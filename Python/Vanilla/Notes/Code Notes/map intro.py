def main():
    yell("This", "is" ,"CS50")

def yell(*words):
    uppercased = map(str.upper, words) # MAP WILL ITERATE EACH OF THE WORD AND CALL UPPER
    print(*uppercased)
    
main()