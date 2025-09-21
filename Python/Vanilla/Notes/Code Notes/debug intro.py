def main():
    height = int(input("Height: "))
    pyramid(height)
    
def pyramid(n):
    for _ in range(n):
        #print(_, end="")
        print("#" * (_+1))
        
if __name__ == "__main__":
      main()