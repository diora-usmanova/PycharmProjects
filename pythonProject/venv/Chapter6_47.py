import turtle
def drawSquare(x,y,side):

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)

def drawFilledSquare(x,y,side):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.end_fill()

startX = -200
startY = 200
turtle.penup()
turtle.goto(startX,startY)
turtle.pendown()
turtle.right(90)

for i in range(0,8):
    if i % 2 == 0:
        drawSquare(startX,startY,30)
    else:
        drawFilledSquare(startX,startY,30)
    startX = startX+30
    turtle.penup()
    turtle.goto(startX,startY)
    turtle.pendown()
    turtle.right(90)
endX = -200
endY = -100
turtle.penup()
turtle.goto(endX,endY)
turtle.pendown()
turtle.right(90)

for i in range(0,8):
    if i % 2 == 0:
        drawSquare(endX,endY,30)
    else:
        drawFilledSquare(endX,endY,30)
    endX = endX+30
    turtle.penup()
    turtle.goto(endX,endY)
    turtle.pendown()
    turtle.right(90)

drawSquare(100,100,30)
drawFilledSquare(150,150,30)
turtle.done()


