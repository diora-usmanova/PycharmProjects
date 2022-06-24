# CHECK A NUMBER
num = eval(input("Enter a integar : "))
print("Is", num, "divisible by 5 and 6 ?",
num % 5 == 0 and num % 6== 0 )
print("Is", num, "divisible by 5 or 6 ?",
 num % 5 == 0 or num % 6 == 0)
print("Is", num, "divisible by 5 or 6 ,
 but not both ?",
          num % 5 == 0 or num % 6 ==0 and not
 (num % 5 == 0 and num % 6 == 0) )


#CLOCK COUNTDOWN
import time
seconds = eval(input("Enter the number of seconds"))
time.sleep(seconds)
if seconds >= seconds - 1:
    print(seconds - 1, "Seconds remaining")
    if seconds >= seconds - 2:
        print(seconds - 2 , "Seconds remaining")
    if seconds == seconds:
        print("Stopped")
#print(seconds)


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


#COMPARE COSTS
firstPackage_weight , price = eval(input
("Enter wiegth and prive for package 1: "))
secondPackage_weight, price2 = eval(input
("Enter weight and price for package 2"))
first_value = price / firstPackage_weight
second_value = price2 / secondPackage_weight
if first_value > second_value:
    print("Package 2 is better price")
else:
    print("First package is better price")


