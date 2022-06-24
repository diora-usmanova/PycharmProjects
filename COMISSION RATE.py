#COMISSION RATE
#annual_salary = eval(input("Enter your goal : "))
base_salary = 5000
for sale in range(500, 30000, 500):
    if sale <= 5000:
        comission = sale * 0.08
    if 5000 <= sale <= 10000:
        comission  = sale * 0.1
    if sale >= 10000:
        comission = sale * 0.12

    #print(sale, comission)
salary = base_salary + comission
print(salary)
#print("To make your goal you have to make : ", 
annual_salary / (12 * salary))
