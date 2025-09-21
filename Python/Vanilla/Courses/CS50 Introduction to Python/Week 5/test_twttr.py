import sys
sys.path.append("/workspaces/73982775/twttr")

from twttr import shorten

def test_vowels():
    assert shorten("blablabla") == "blblbl"
    assert shorten("nigga") == "ngg"
    assert shorten("AIEUO") == ""
    assert shorten("aeuio") == ""

def test_consonants():
    assert shorten("i hte ngga") == " ht ngg"
    assert shorten("XQC") == "XQC"

def test_numbers():
    assert shorten("123") == "123"
    assert shorten("Ni334") == "N334"

def test_mixed():
    assert shorten("Hello, My Nigga 360!") == "Hll, My Ngg 360!"


