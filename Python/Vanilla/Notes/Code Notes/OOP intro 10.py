class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient # WE CAN ACCESS THESE 4 later on
        self.weight = weight
                 
                 
def main(): # Ways to store information 
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]

main()
