# POPULATION PROJECTION
birth = 60 / 7
death = 60 / 13
immigration = 60 / 45
population = 312032486
minutes_in_a_year = 365 * 24 * 60
years = eval(input("Enter the number of years: "))
change = ((birth + immigration)-death)
total = population + (minutes_in_a_year * change) * years
print("Population in ", years, " will be ", round(total))
print ("Difference is ", round(total - population))


