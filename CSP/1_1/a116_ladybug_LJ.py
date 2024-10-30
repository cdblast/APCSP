#   a116_ladybug.py
import turtle as trtl

wn = trtl.Screen()

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(2)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots = num_dots + 1

  # position next dots
  ypos = ypos + 24
  xpos = xpos + 3
  num_dot = num_dots + 1

ladybug.hideturtle()

wn.mainloop()