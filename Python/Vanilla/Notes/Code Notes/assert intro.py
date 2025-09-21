import sys
sys.path.append(r"D:\College\Coding Files\Latihan\Learn Language\Python")  # Use raw string or double backslashes

from EvanScript import square  

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4 # TO assert and check that square2 MUST BE 4!
        assert square(3) == 9
        assert square(-2) == 4
        assert square(-3) == 9
        assert square(0) == 0
    except AssertionError: # Error that show up when assert is incorrect!
        print("Stupid")
        


if __name__ == "__main__":  
    main()

