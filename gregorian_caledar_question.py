year = int(input("Enter the year : "))

if year < 1582 :
    print(year, "is not in Gregorian period.")
elif year % 4 != 0 :
    print(year, "is a common year.")
elif year % 100 != 0 :
    print(year, "is a leap year.")
elif year % 400 != 0 :
    print(year, "is a common year.")
else :
    print(year, "is a leap year.")