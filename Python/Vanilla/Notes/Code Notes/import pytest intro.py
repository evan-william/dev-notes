import sys
sys.path.append(r"D:\College\Coding Files\Latihan\Learn Language\Python")  # Use raw string or double backslashes

from EvanScript import square  
import pytest

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    # assert square("cat") ==
    # assert convert(0,001) == pytest.approx(149blablablba) APPROX IS TO TEST FLOAT LIKE APPROXIMATELY
    # assert convert(0,001) == pytest.approx(149blablablba, abs = 0.1) abs = 0.1 or also abs =1e-2 is also available  so that gives more tolerance
    
# def test_positive , test_negative, test_zero ((This will shoow all the error instead of just showing 1 error then stop because
# we put everything in 1 function before

def test_str():
    with pytest.raises(TypeError):
        square("cat")
    
# Try pytest (name of the file).py
# FOR EXAMPLE == pytest test_calculator.py
