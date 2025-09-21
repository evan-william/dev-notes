import csv

people = []

with open("names3.csv") as ANYTHING:
    reader = csv.DictReader(ANYTHING) # DICT reader is to read a csv file includes commas etc etc
    for row in reader:     # THIS WILL LOAD IT AS A DICT OF COLUMNS AND NOT A LIST OF COLUMNS
        people.append({"name": row["name"], "gender": row["gender"], "major": row["major"]})       
    # CAN DO
    # for row in reader:
    #    people.append({"name": row[0], "gender": row[1]})
# THIS IS WHERE THE LIST/DICT SORTING BEGINS
for _ in sorted(people, key=lambda _: _["name"]):
    print(f"{_['name']} is {_['gender']} and majors {_['major']}")
    
    
