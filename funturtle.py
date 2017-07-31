import turtle
##turtle.shape('turtle')
##square=turtle.clone()
##square.shape('square')
##square.goto(100,0)
##square.goto(100,100)
##square.goto(0,100)
##square.goto(0,0)
##
##triangle=turtle.clone()
##triangle.shape('triangle')
##triangle.penup()
##triangle.goto(-100,0)
##triangle.pendown()
##triangle.goto(-200,0)
##triangle.goto(-150,100)
##triangle.goto(-100,0)
##
##square.penup()
##square.goto(300,300)
##square.pendown()
##square.stamp
turtle.goto(100,100)

UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
SPACEBAR="space"

UP=0
LEFT=1
DOWN=2
RIGHT=3
direction=UP
def up():
    global direction
    direction=0
    old_pos=turtle.pos()
    x,y=old_pos
    turtle.goto(x,y+10)

    print(turtle.pos())

def down():
    global direction
    direction=2
    old_pos=turtle.pos()
    x,y=old_pos
    turtle.goto(x,y-10)

    print(turtle.pos())

    
   
    
def left():
    global direction
    direction=1
    old_pos=turtle.pos()
    x,y=old_pos
    turtle.goto(x-10,y)

    print(turtle.pos())

    
    
def right():
    global direction
    direction=3
    old_pos=turtle.pos()
    x,y=old_pos
    turtle.goto(x+10,y)

    print(turtle.pos())

   


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()






    









turtle.mainloop()
