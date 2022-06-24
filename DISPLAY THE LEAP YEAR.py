#DISPLAYING THE LEAP YEAR
years_per_line  = 10
count = 0
for year in range(2000, 2100):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        count += 1
        print(format(year, "5d"), end = '')
        if count % years_per_line == 0:
            print()