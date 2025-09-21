import csv

people = []

with open("names2.csv") as ANYTHING:
    reader = csv.reader(ANYTHING) # reader is to read a csv file includes commas etc etc
    for name, gender in reader:
        people.append({"name": name, "gender": gender})       
    # CAN DO
    # for row in reader:
    #    people.append({"name": row[0], "gender": row[1]})
# THIS IS WHERE THE LIST/DICT SORTING BEGINS
for _ in sorted(people, key=lambda _: _["name"]):
    print(f"{_['name']} is {_['gender']}")
    
    