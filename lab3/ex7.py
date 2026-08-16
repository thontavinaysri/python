#25341a05l1 vinay
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid date")

else:
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            mday = 29
        else:
            mday = 28

    elif month == 4 or month == 6 or month == 9 or month == 11:
        mday = 30

    else:
        mday = 31

    if day >= 1 and day <= mday:
        print("Valid date")
    else:
        print("Invalid date")

        ''' output
        Enter year: 2024
Enter month: 13
Enter day: 34
Invalid date
'''