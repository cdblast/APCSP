#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50

for s in turtle_shapes:
# picks shape
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
#gives horizontal list the turtleshape its using
  ht.penup()
  new_color = horiz_colors.pop()
#takes color out of horiz_colors list
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50


for step in range(50):
  for ht in horiz_turtles:
    for vt in vert_turtles:
      ht.forward(3)
      vt.forward(3)
      if (abs(ht.xcor() - vt.xcor()) < 30):
        if (abs(ht.ycor() - vt.ycor()) < 30):
          vert_turtles.remove(vt)
          horiz_turtles.remove(ht)

wn = trtl.Screen()
wn.mainloop()
