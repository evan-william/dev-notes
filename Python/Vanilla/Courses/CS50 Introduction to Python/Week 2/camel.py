def convert(camelname):
    snakecase = camelname[0].lower()
    for char in camelname[1:]:
         if char.isupper():
            snakecase += "_" + char.lower()
         else:
            snakecase += char
    print("snake_case:",snakecase,end="")
    print()

camelname = input("camelCase: ").strip()
convert(camelname)