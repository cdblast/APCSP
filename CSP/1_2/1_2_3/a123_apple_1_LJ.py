#   a123_apple_1_LJ.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif"
pear_image = "pear.gif"
# Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)

# Established lists :3
letters = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']

appleList = []
appleLetters = []
fruit = [apple_image, pear_image]

# five apples on the screen
for i in range(5):
  appleList.append(trtl.Turtle())
  appleLetters.append(rand.choice(letters))
  fruit.append(rand.choice(fruit))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

# draw apple function
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

# drop apple function
def drop_apple(index):
  appleList[index].pu()
  appleList[index].clear()
  appleList[index].sety(-150)
  appleList[index].hideturtle()
  appleLetters[index] = rand.choice(letters)
  draw_apple(index)

# key functions
def typeda():
  for i in range(5):
    if appleLetters[i] == 'A':
      drop_apple(i)

def typeds():
  for i in range(5):
    if appleLetters[i] == 'S':
      drop_apple(i)

def typedd():
  for i in range(5):
    if appleLetters[i] == 'D':
      drop_apple(i)

def typedf():
  for i in range(5):
    if appleLetters[i] == 'F':
      drop_apple(i)

def typedg():
  for i in range(5):
    if appleLetters[i] == 'G':
      drop_apple(i)

def typedh():
  for i in range(5):
    if appleLetters[i] == 'H':
      drop_apple(i)

def typedj():
  for i in range(5):
    if appleLetters[i] == 'J':
      drop_apple(i)

def typedk():
  for i in range(5):
    if appleLetters[i] == 'K':
      drop_apple(i)

def typedl():
  for i in range(5):
    if appleLetters[i] == 'L':
      drop_apple(i)

#-----function calls-----
for i in range(5):
  draw_apple(i)
wn.onkeypress(typeda, 'a')
wn.onkeypress(typeds, 's')
wn.onkeypress(typedd, 'd')
wn.onkeypress(typedf, 'f')
wn.onkeypress(typedg, 'g')
wn.onkeypress(typedh, 'h')
wn.onkeypress(typedj, 'j')
wn.onkeypress(typedk, 'k')
wn.onkeypress(typedl, 'l')
wn.listen()
wn.mainloop()