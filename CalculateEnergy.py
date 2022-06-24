# CALCULATE ENERGY

water = eval(input("Enter the amount of water in kg "))
init_temper = eval(input("Enter initial temperature: "))
final_temp = eval(input("Enter the final temperature: "))
energy = water *(final_temp - init_temper) * 4184
print("the Energy needed is ", energy)
