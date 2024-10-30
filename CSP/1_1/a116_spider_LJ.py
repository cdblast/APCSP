#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

wn = trtl.Screen()

trtl = trtl.Turtle()

trtl.pensize(30)
trtl.goto(6,15)
trtl.stamp()

#spider body
trtl.color("black")
trtl.penup()
trtl.goto(0,0)
trtl.pendown()
trtl.circle(20)
            
#spider head
trtl.penup()
trtl.goto(30,10)
trtl.pendown()
trtl.circle(10)

trtl.color("black")

legCount = 8 #the amount of legs you want
legLength = 50 #how long the legs are
legSpace = 200 / legCount #spacing between legs
trtl.pensize(6)
loopCounter = 0
#there are 6 legs. make 8 
#make sure to position the legs properly
trtl.penup()
while (loopCounter < legCount):
  trtl.goto(-1,30)
  trtl.pendown()
  trtl.setheading(legSpace*loopCounter + 180)
  trtl.circle(100,legLength)
  #trtl.forward(legLength)
  trtl.penup()
  loopCounter = loopCounter + 1
  if (loopCounter == 4):
    legLength = -legLength

#eyes
trtl.color("white")
trtl.goto(30,19)
trtl.pendown()
trtl.forward(1)
trtl.penup()

trtl.lt(140)
trtl.penup()
trtl.forward(10)
trtl.pendown()
trtl.forward(1)

trtl.hideturtle()

wn.mainloop()