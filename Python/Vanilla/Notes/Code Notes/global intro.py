balance = 0
# UnboundLocalError will raise when printing this because
# A global variable CANNOT be change outside its local function like at line 11 and 14
# A global variable can only be read 

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)
    
def deposit(number):
    global balance # ADD THIS global balance LINE SO GLOBAL IS ACCESABLE WITH LOCAL FUNCTION
    balance += number
    
def withdraw(number):
    global balance    # WITHOUT THIS IT WONT WORK
    balance -= number


if __name__ == "__main__":
    main()