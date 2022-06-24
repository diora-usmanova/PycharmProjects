# FROM FEET TO METERS
'''foot = eval(input("Enter a value for feet : "))
meter = foot * 0.305
print(foot, " feet is ", meter, "meters" )'''

# FROM MILES TO KILOMETERS
'''print("Miles            Kilometers")
for i in range(1,11):
    print(i, format(i * 1.609, ">23.3f"))'''

# FROM MILES TO KM, FROM KM TO MILES
print("miles       kilometers    |     kilometers           miles")
kilometers = 20
for i in range(1, 11):
    print(i, format(i * 1.609, ">20.3f"), "   |     ", kilometers, format(kilometers * 0.621, ">23.3f"))
    kilometers += 5
