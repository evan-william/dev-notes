import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM!") == 1

def test_multiple_um():
    assert count("um um") == 2
    assert count("Um, thanks, um...") == 2
    assert count("um? um. um!") == 3

def test_um_as_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("document") == 0

def test_um_with_punctuation():
    assert count("Um, hello!") == 1
    assert count("Um... what?") == 1
    assert count("Um? Um.") == 2

def test_um_in_sentence():
    assert count("Hello, um, how are you?") == 1
    assert count("Um, I think, um, we should go.") == 2
    assert count("That's um... interesting.") == 1
