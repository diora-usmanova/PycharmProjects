
# COMPUTE DISTANCE BETWEEN POINTS

def distance (x1,y1, x2,y2):
    return((x1-x2)**2 +(y1-y2)**2)**0.5
x1,y1,x2,y2 = (eval(input("Enter 4 points: ")))
print(distance(x1,y1,x2,y2))

