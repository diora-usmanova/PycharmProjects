# 1.8
'''radius = 5.5
PI = 3.1415
area = radius * radius * PI
perimeter = 2 * radius * PI
print(area)
print(perimeter)

# 1.9
width = 4.5
height = 7.9
area = width * height
print(area)

# 1.10
average = 60 / 45.5
kilometers_per_hour = average * 14
miles_per_hour = kilometers_per_hour / 1.6
print(miles_per_hour)'''

# Ch2-1

'''celsius = eval(input("Enter a degree in  celsius"))
fahrenheit = (9 / 5) * celsius + 32
print(celsius, "Celsius is ", fahrenheit, "Fahrenheit")'''

# Ch2_2
'''radius, length = eval(input("Enter the radius and length :"))
PI = 3.1415
area = radius * radius * PI
volume = area * length
print("Area is : ", area)
print("The volume is ", volume)'''

# Ch2_3
'''feet = eval(input("Enter a value for feet: "))
meters = feet * 0.305
print(feet, "feet is ", meters, "meters")'''

# Ch2_5 CALCULATE TIPS
'''subtotal, gratuity_rate = eval(input("Enter a subtotal and gratuity rate : "))
gratuity = subtotal * ( gratuity_rate / 100)
total = subtotal + gratuity
print("The gratuity is ", gratuity, " and the total is ", total)'''

'''values = [[3, 4, 5, 1], [33, 6, 1, 2]]

v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]

print(len(values))
print(values[row] )

print(values[row][column])
print(len(values[row]))
print(v)'''

'''values = [[3, 4, 5, 1], [33, 6, 1, 2]]

v = values[0][0]
print(v)
for lst in values:
    for element in lst:
        if v > element:
            v = element


print(lst)
print(element)
print(v)'''

# values = [[3, 4, 5, 1], [33, 6, 1, 2]]

'''for row in values:
    row.sort()
    for element in row:
        print(element, end = " ")
    print()'''

# adding columns
# matrix = [[1, 2, 3, 4],
# [3, 4, 5, 6]]

'''for j in range(0, len(matrix[0])):
    s = 0
    for i in range(0, len(matrix)):
        s += matrix[i][j]
    print(s)
    s = 0'''

# RANDOM SHUFFLING
import random

'''for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        randI = random.randrange(0, len(matrix))
        randJ = random.randrange(0, len(matrix[i]))
        matrix[i][j], matrix[randI][randJ] = matrix[randI][randJ], matrix[i][j]
print(matrix)'''

# passing to Function
'''def increment(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] += 1
    return matrix


matrix = [[1, 2, 3, 4], [4, 5, 6, 7]]
m = increment(matrix)

print(id(matrix))
print(id(m))'''

# MULTIDIMENSIONAL LIST
'''matrix = [[1, 2],[ 3, 4]],[ [4, 5], [6, 7]]
print(len(matrix))
print(len(matrix[0]))
print(len(matrix[0][1]))'''

# CHECKING GRADE
'''students = [['A'], ['B'], ['D'],
            ['A'], ['C'], ['D'],
            ['B'],['D'], ['A']]
            
         
         
         
         
         
         
         
         
         
         
         
         
            '''
# cHAPTER 13
'''l1 = [1,2,3]
try:
    print(l1[10])
except:
    print("Problem happened")

print("hello")'''

# TUPLES are inmutabale, cannot make a change
'''t1 = () # CREATING TUPLE
t1 = (1, 3, 4, 5)
print(type(t1))
print(len(t1))
print(sum(t1))
print(t1[0])

t2 = tuple([3,2,1,4])
print(t2)
l1 = list(t2)
print(l1)
print(2 in t1)'''

#SETS is like list, but there is no order in set, cannot have a duplicates

'''s1 = {1,2,3,4,6}
print(s1)
s2 = set([1,2,3,4,2]) # create a set from tuple, takes out the duplicates
print(s2)
s1.symmetric_difference(s2)
print(s1)'''

#DICTIONARY
d1 = {123:"Hello", 567: "Python", "Java" : 98473}
print(len(d1))
print(d1[123]) # VALUE IF THE KEY
print(d1["Java"])
d1[1111] = "C#" # adding a value
#print(d1["C#"])
del d1[123] # deleting a value
print(d1)
for k in d1:
    print(k, d1[k])

for items in d1.keys():
    print(items)

print(d1[123])
print(d1.get(123))



