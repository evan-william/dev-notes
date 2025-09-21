import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    # 9:00 AM to 5 PM
    # 9 AM to 5:00 PM
    pattern = r"^([1-9]|1[1-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[1-2])(:[0-5][0-9])? (AM|PM)$"
    match = re.search(pattern, s)
    try:
        if match:
            hour1 = match.group(1)
            min1 = match.group(2)
            AMPM1 = match.group(3)
            hour2 = match.group(4)
            min2 = match.group(5)
            AMPM2 = match.group(6)

            if AMPM1 == "AM":
                if int(hour1) == 12:
                    hour1 = 0
                else:
                    hour1 = int(hour1)
            else:
                if int(hour1) == 12:
                    hour1 = 12
                else:
                    hour1 = int(hour1) + 12

            if AMPM2 == "AM":
                if int(hour2) == 12:
                    hour2 = 0
                else:
                    hour2 = int(hour2)
            else:
                if int(hour2) == 12:
                    hour2 = 12
                else:
                    hour2 = int(hour2) + 12

            if min1 == None:
                min1 = ":00"
            else:
                min1 = min1

            if min2 == None:
                min2 = ":00"
            else:
                min2 = min2

            return f"{hour1:02}{min1} to {hour2:02}{min2}"

        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")

if __name__ == "__main__":
    main()
