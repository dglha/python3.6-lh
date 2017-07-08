import calendar
year = int(input("Enter year: "))
if 1>year or year >99999:
    print("please choose another year")
else:
    for i in range (12):
            print(calendar.month(year,i+1))