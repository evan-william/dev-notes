import bank
from bank import value

def test20():
    assert value("hibba") == 20
    assert value("higga") == 20
    assert value("hendra") == 20

def test0():
    assert value("Hello") == 0
    assert value("hello") == 0

def test100():
    assert value("chigga") == 100
