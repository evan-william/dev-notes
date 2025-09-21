class Account:
    def __init__(self):
        self._balance = 0 # Instance variable  # "_" means private
            # THIS ALSO MAKES IT ACCESSIBLE TO ALL METHODS
                           
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance += n
    
    def withdraw(self, n):
        self ._balance -= n
        
def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:" , account.balance)
    
if __name__ == "__main__":
    main()
        