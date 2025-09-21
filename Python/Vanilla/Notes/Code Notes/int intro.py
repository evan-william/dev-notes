# DO NOT DO THIS BECAUSE THIS ONLY COMBINES THE INT
x = input("What's X? ")
y = input("What's Y? ")

z = x + y
print(z)

# DO THIS INSTEAD
x = input("What's X? ")
y = input("What's Y? ")

z = int(x) + int(y)
print(z)

# CAN ALSO DO THIS
x = int(input("What's X? " ))
y = int(input("What's Y? "))

print("The Total is", (x + y))

# AND LASTLY THIS
print(int(input("What's X? ")) + int(input("What's Y? ")))

# OTHER THAN INT CAN ALSO USE FLOAT
a = float(input("What's A? "))
b = float(input("What's B? "))

c = round(a + b)
print(c)
    
# THERES A WAY TO SPECIFY COMA
a = float(input("What's A? "))
b = float(input("What's B? "))

c = round(a + b)
print(f"{c:,}")

# COMA SPECIFY LOCATION
a = float(input("What's A? "))
b = float(input("What's B? "))

c = a / b
print(f"{c:.2f}")
