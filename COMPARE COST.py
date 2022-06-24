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


