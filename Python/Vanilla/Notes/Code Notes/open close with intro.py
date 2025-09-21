"""
name = input("What's your name? ")

file = open("names.txt", "w") # w = write
file.write(name) # A FUNCTION THAT COMES WITH IT
file.close() # CLOSES THE FILE
"""
# THIS ABOVE WILL JUST CREATE AND REWRITE EACH TIME , NOT RECOMMENDED


"""
name = input("What's your name? ")

file = open("names.txt", "a") # a = append
file.write(name) # A FUNCTION THAT COMES WITH IT
file.close() # CLOSES THE FILE
"""
# THIS ABOVE WILL APPEND FOR EXAMPLE 3 names , Evan Jen Budijono will become appended to EvanJenBudijono



name = input("What's your name? ")

file = open("names.txt", "a") # a = write
file.write(f"{name}\n") # A FUNCTION THAT COMES WITH IT , THIS IS A BETTER VERSION THAT WILL FIX THE APPEND ISSUE
file.close() # CLOSES THE FILE

# THIS IS THE ONE U WANT , FILE MUST BE CLOSE WITH FILE.CLOSE OR names.txt might get corrupted

"""
name = input("What's your name? ")

with open("names.txt" , "a") as file  # OPEN ACTS AS A SHORTER AND BETTER ALT VERSION TO CLOSE
    file.write(f"{name}\n")		 # AS LONG AS NOTHING MORE INDENTED IN WITH , IT WILL AUTO COSE THE TEXT SO FILE.CLOSE IS NOT NEEDED
"""

