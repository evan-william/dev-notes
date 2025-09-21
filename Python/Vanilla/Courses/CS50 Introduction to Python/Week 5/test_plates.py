import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("PYTHON") == True
    assert is_valid("AB1234") == True

def test_invalid_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_invalid_start():
    assert is_valid("50CS") == False
    assert is_valid("123ABC") == False

def test_invalid_number_placement():
    assert is_valid("CS50P") == False
    assert is_valid("AA22A") == False

def test_invalid_zero():
    assert is_valid("CS05") == False
    assert is_valid("AB0123") == False

def test_invalid_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("HEL-LO") == False
    assert is_valid("NO SPACE") == False
