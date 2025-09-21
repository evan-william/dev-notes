#Testing
print("Hello World")
name = input("Whats your name? ")
print("Hello,",name)

#print(*objects, sep=' ', end='\n') <--- Parameter
print("Hello, ", end="")
print(name)

print("Hello, ",name,sep="Nigga ")

print('Hello, "friend"')
print("Hello, \"friend\"")

print(f"Hello, {name}") # <---- f will read the spesial format!

# Remove Whitespeace from Str
age = input("How old are you? ")
age = age.strip()

# Auto Capitalize FIRST letters
gender = input("What is your gender? ")
gender = gender.capitalize()

print(f"{gender} confirmed")

# Auto Capitalize Letters + Remove Whitespace
text = input('Please type "iam smart"= ')
text = text.title().strip()

print(f"You said : {text}")

# Compile Everything is okay
name2 = input("Please re enter your name = ").strip().title()
print(f"Your name is = {name2}")

#lstrip and rstrip is also available

#Split user's name into first name and last name
name3 = input("Please enter 3 words name = ").strip().title()
first, middle, last = name3.split("Nigga")

print(f"Hello, {first}")
print(f"Hello, {middle}")
print(f"Hello, {last}")

"""
Test Comment
"""