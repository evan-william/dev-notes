def main():
    soldier = input("")
    soldierHeight = list(map(int, input("").split(","))) # ['11','22','33','44']
    heightCheck(soldierHeight)
    
def heightCheck():
    ...
    # The map() function applies a given function (in this case, int) to every item in an iterable (our list of strings).
    # Converts the map object into an actual list of integers.