def main():
    print_square(6)

def print_square(size):
    # For each row in squre
    for Row in range(size):
        # For each brick in row
        for Brick in range (size):
            # Print brick
            print("#", end="")
        print()
        
main()


def print_square(size):
    for i in range(size):
        print("#" * size)
        
main()
        
