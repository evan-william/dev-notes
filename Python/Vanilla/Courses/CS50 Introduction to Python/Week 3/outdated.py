def main():
    datelist = {
        "January" : "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    while True:
        try:
            date = input("date: ").capitalize().strip('"')
            if date[0].isdigit():
                day, month, year = date.split("/")
                if day.isdigit() and month.isdigit() and year.isdigit():
                    if 1 <= int(day) <= 12 and 1 <= int(month) <= 31:
                        print(f"{year}-{int(day):02d}-{int(month):02d}") # Day and Month here switched , too lazy to fix
                        break
                    else:
                        pass
                else:
                    pass
            elif date[0].isalpha():
                daymonth, year = date.split(",")
                month, day = daymonth.split()
                if 1 <= int(day) <= 31:
                    print(f"{year.strip()}-{datelist[month.title()]}-{int(day):02d}")
                    break
                else:
                    pass
            else:
                pass

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
main()
