import turtle

turtle.bgcolor("black")
turtle.pensize(2)

a=turtle.Turtle()
a.penup()
a.goto(-250,45)
a.pendown()
style=('courier',80,'bold')
a.color("yellow")
a.write('I',font=style,align='center')
a.hideturtle()

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red","pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.0)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

a=turtle.Turtle()
a.penup()
a.goto(280,60)
a.pendown()
a.color("yellow")
style=('courier',80,'bold')
a.write('you',font=style,align='center')
a.hideturtle()



a=turtle.Turtle()
a.penup()
a.isdown()
a.goto(0, -130)
style=('courier',80,'bold')
a.color('blue')
a.write('Wulan', font=style, align='center')
a.hideturtle()

turtle.done()