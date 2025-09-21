# Useable but incorrect
def main():
    time = input("What time is it? = ")
    print(f"{convert(time)}")


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
   
    complete = float(int(hours) + float(minutes))
    # print(complete)
  
    if 7 <= complete <= 8:
        return "breakfast time"
    elif 12 <= complete <= 13:
        return "lunch time"
    elif 18 <= complete <= 19:
        return "dinner time"
    else:
        return ""
    
main()


# Same thing but correct
def main():
    time = input("What time is it? ")
    decimal_time = convert(time)  

    if 7 <= decimal_time <= 8:
        print("breakfast time")
    elif 12 <= decimal_time <= 13:
        print("lunch time")
    elif 18 <= decimal_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
