#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  append moves each "s" out of turtle_shapes and into my_turtles.
startx = 0
starty = 0

direction = 0

#each turtle waits seperately until then they go to start coordinates, then move to the right and stay there.
for t in my_turtles:
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)

  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.right(45)     
  t.forward(50)
  t.penup()


#	Start gets changed, which is why every turtle is diagonally moved upwards and to the right.
  direction = t.heading()
  startx = t.xcor()
  starty = t.ycor()
  

wn = trtl.Screen()
wn.mainloop()