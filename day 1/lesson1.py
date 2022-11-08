from turtle import*

#square

speed(30)
width(7)
color("green")
forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

#roof
color("purple")
begin_fill()
left(60)
forward(200)
right(120)
forward(200)
end_fill()

#door

penup()
goto(75, -200)
pendown()

begin_fill()
left(-210)
forward(100)

right(90)
forward(50)

right(90)
forward(100)
end_fill()


# window1

penup()
goto(70, -25)
pendown()

begin_fill()
forward(50)
left(-90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

# window2

penup()
goto(130, -25)
pendown()


begin_fill()
forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)
end_fill()



exitonclick()