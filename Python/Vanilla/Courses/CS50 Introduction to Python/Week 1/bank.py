def main():
    greeting= input("Greeting= ").strip().lower()
    print(f"${startexe(greeting)}")

def startexe(greeting):
    greeting = greeting.split()[0]
    greeting = greeting.rstrip(",")
    
    if greeting.startswith("h") and greeting != "hello":
        return 20
    elif greeting.startswith("hello"):
        return 0
    else:
        return 100

main()




