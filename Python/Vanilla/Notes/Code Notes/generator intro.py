def main():
    n = int(input("What's n? "))
    for s in scared(n):
        print(s)

""" DOING THIS WHEN PRINTING 1MILLION , WILL CRASH AND FAILED
def scared(n):
    man = []
    for i in range(n):
        man.append("😱" * i)
    return man
"""
def scared(n):
    for i in range(n):
        yield "😱" * i


main()