import inflect

p = inflect.engine() # A Must , p can be anything

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
        
except EOFError:
    pass

combine = p.join(names)
print(f"Adieu, adieu, to {combine}")

