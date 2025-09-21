"""Meow n times.""" # """ Comment can be diagonal or vertial line formed

""" # THIS CALLED DOCSTRING 
Meow n times.

:param n: number of times to meow
:type n: int
:raise TypeError: if n is not an int
:return: A string of n meows, one per line
:rtype: str
"""


def test():
    return f"""
        =============
        hello my friend
        are you okay?
        =============
        """

print(f"{test()}")

