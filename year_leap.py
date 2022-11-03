def year_leap():
    year=int(input("Enter a year: "))
    if (year % 4==0 and year %100 != 0)or year % 400==0:
        return(year,"It's leap year")
    else:
        return(year,"It's not year")

print(year_leap())

