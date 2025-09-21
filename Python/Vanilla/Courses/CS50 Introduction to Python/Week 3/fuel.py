def main():
    fraction = getfraction()
    print(fraction)

def getfraction():
    while True:
        try:
            fraction = input("Fraction: ")
            first, last = fraction.split("/")

            first, last = int(first), int(last)

            if last > first or last == first:
                convert = int(first) / int(last)
                if convert <= 0.01:
                    return "E"
                elif 1 >= convert >= 0.99:
                    return "F"
                else:
                    convert2 = convert * 100
                    convert2 = f"{round(convert2)}%"
                    return str(convert2)
            else:
                pass

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()


