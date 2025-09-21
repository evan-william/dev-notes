import csv

name = input("What's your name? ").strip()
home = input("Where's your home? ").strip()

with open("names5.csv", "a", newline="") as ANYTHING: # NEWLINE PREVENTS UNWANTED EMPTY LINES
    ANYTHING2 = csv.DictWriter(ANYTHING, fieldnames=["name", "home"]) # List actual columns that yo know are in this file
    ANYTHING2.writerow({"name": name, "home": home})