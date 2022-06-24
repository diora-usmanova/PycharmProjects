# NUMBERS OF DAYS IN A MONTH
month_number = eval(input("Enter a month number: "))
year = int(input("Enter a year: "))
if month_number in [1, 3, 5, 7, 8, 10, 12]:
    num_days = 31
elif month_number in [4, 6, 9, 11]:
    num_days = 30
else:
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        num_days = 29
    else:
        num_days = 28
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
print(month[month_number - 1], year, "has", num_days, "days")
