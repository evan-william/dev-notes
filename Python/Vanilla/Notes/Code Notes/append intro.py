name1 = []

for _ in range(3):
    name = input("What's your name? ")  
    name1.append(name)
    
    # OR CAN DO names.append(input("What's your name? "))
    
for _ in sorted(name1): # SORT IT IN ALPHABETICAL ORDER
    print(f"hello, {_}")
    

    

    

