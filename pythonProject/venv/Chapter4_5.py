today = eval(input("Enter today's date : "))
numberOfDays = (eval(input("Enter the number of days elapsed since today: ")))
if today ==0:
    print("Today is Sunday")
elif today == 1:
    print("Today is Monday")
elif today  == 2:
    print("Today is Tuesday")
elif  today == 3:
    print("Today is Wednesday")
elif today == 4:
    print("Today is Thursday")
elif today == 5:
    print("Today is Friday")
elif today ==  6:
    print("Today is Saturday")
else:
    print("Wrong Entry")
    
futureDay = (today+numberOfDays) % 7
if futureDay == 0:
    print(" and future day will be Sunday")
elif futureDay== 1:
    print(" and future day will be Monday")
elif futureDay  == 2:
    print(" and future day will be Tuesday")
elif  futureDay == 3:
    print(" and future day will be Wednesday")
elif futureDay == 4:
    print(" and future day will be Thursday")
elif futureDay == 5:
    print(" and future day will be Friday")
elif futureDay ==  6:
    print(" and future day will be Saturday")
else:
    print("Wrong Entry")



