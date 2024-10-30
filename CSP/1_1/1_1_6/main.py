#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

#originally trtl.zcreen waz at the bottom but i moved it up ^_^
wn = trtl.Screen()

trtl = trtl.Turtle()

trtl.pensize(30)
# Spider red spot
trtl.color("red")
trtl.goto(5,20)
trtl.forward(1)

#spider body
trtl.color("black")
trtl.penup()
trtl.goto(0,0)
trtl.pendown()
trtl.circle(20)

legCount = 8 #the amount of legs you want
legLength = 90 #how long the legs are
legSpace = 300 / legCount #spacing between legs
trtl.pensize(6)
loopCounter = 0
#there are 6 legs. make 8 
#make sure to position the legs properly
trtl.penup()
while (loopCounter < legCount):
  trtl.goto(-1,30)
  trtl.pendown()
  trtl.setheading(legSpace*loopCounter)
  trtl.forward(legLength)
  trtl.penup()
  loopCounter = loopCounter + 1
trtl.hideturtle()

wn.mainloop()