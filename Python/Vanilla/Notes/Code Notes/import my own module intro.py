import sys
sys.path.append(r"D:\College\Coding Files\Latihan\Learn Language\Python")  # Use raw string or double backslashes

from EvanScript import square  

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")  
    if square(3) != 9:
        print("3 squared was not 9")
        


if __name__ == "__main__":  
    main()
