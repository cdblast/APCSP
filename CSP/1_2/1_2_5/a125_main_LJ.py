# a125_main_LJ.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
wn = trtl.Screen()
wn.bgcolor("white smoke")

#sprites
flowerhead = "flowerhead.gif"
petal = "petalpart.gif"
wn.addshape(flowerhead) # Make the screen aware of the new file
wn.addshape(petal)

trtl.register_shape(petal, shape="petalpart.gif")

petal_timesclicked = 0

Petals = []

petalamount = rand.randint(5,15)
petalangle = 360/petalamount


#-----initialize turtle-----
rands = rand.Random()
turtl = trtl.Turtle()

flowerhead = trtl.Turtle(shape=flowerhead)

#crush = input("Who's your crush?")

#-----game functions--------
def petalclicked():
  #if mod operator timesclicked odd Loves me if even Loves me not
  print("ahhh!!")  

def startgame():
  #make flower() (this is gonna be just the flower head lol.)
  #make petals() (function should have random generated and the petals should be either clicked or spacebar to pop off.)
  print("help me!!")

def petalgen():
  global petalamount
  global petalangle
  loopcount = 0
  for i in range(petalamount):
    Petals.append(trtl.Turtle(shape=petal))
    trtl.penup()
    trtl.setheading(petalangle*loopcount)
    trtl.forward(50)
    loopcount += 1

'''
def draw_apple(index):
  global appleLetter
  appleList[index].penup()
  appleList[index].shape(rand.choice(fruit))
  wn.tracer(False)
  appleList[index].setx(rand.randint(-175, 175)) #reset apple
  appleList[index].sety(rand.randint(-25, 100)) #reset apple

  appleList[index].sety(appleList[index].ycor()-35)
  appleList[index].color("white")
  appleList[index].write(appleLetters[index], align="center", font=("Arial", 40, "bold"))
  appleList[index].sety(appleList[index].ycor()+35)
  appleList[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  appleList[index].pu()
  appleList[index].clear()
  appleList[index].sety(-150)
  appleList[index].hideturtle()
  appleLetters[index] = rand.choice(letters)
  draw_apple(index)

def typedf():
  for i in range(5):
    if appleLetters[i] == 'A':
      drop_apple(i)

'''
#-----events----------------

#startgame()
petalgen()
wn.onkeypress(petalclicked,"f")
wn.listen
wn.mainloop()
