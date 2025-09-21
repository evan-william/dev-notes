people = []

with open("names.csv") as ANYTHING:
    for _ in ANYTHING:
        name, gender = _.rstrip().split(",")
        human = {"name": name,"gender" : gender}
        people.append(human)
        
def get_name(human):
    return human["name"]

def get_gender(human):
    return human["gender"]

# THIS IS WHERE THE LIST/DICT SORTING BEGINS
for _ in sorted(people, key=get_gender): 
    print(f"{_['name']} is {_['gender']}")
    
    
"""    # THE USAGE OF LAMBA MEANS THAT THE FUNCTION NO NEED NAME AND ONLY BE CALLED ONCE

with open("names.csv") as ANYTHING:
    for _ in ANYTHING:
        name, gender = _.rstrip().split(",")
        human = {"name": name,"gender" : gender}
        people.append(human)
        
def get_name(human):
    return human["name"]

def get_gender(human):
    return human["gender"]

# THIS IS WHERE THE LIST/DICT SORTING BEGINS
for _ in sorted(people, key=lambda _: _["name"]):
    print(f"{_['name']} is {_['gender']}")
""" 
    
    
