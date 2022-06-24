import turtle
P = 3.1415
x,y = eval(input("enter the center of the circle : "))
radius = eval(input("Enter the radius of the circle : "))
area  = (radius* radius)*P
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.circle(radius)
# turtle.goto((x+radius),(y+radius))
turtle.write(area)
turtle.done()
