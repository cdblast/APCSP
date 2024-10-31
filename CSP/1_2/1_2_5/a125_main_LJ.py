# a125_main_LJ.py
'''
  OK so the idea is
  -cute art/sprites (last)
  -background (nice to have)

  petals randomized (hopefully we can set origin of each sprite to the center and make rotation dependent on randomized petal count)
  create flower

  what is the name?
  loves me, loves me not.. each time petal is plucked (using space bar i think)s
'''
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

petal_timesclicked = 0
crush = " "

Petals = []

petalamount = rand.randint(5,15)


#-----initialize turtle-----
rands = rand.Random()
turtl = trtl.Turtle()

flowerhead = trtl.Turtle(shape=flowerhead)
flowerhead.penup()

#-----game functions--------

def startgame():
  crush = input("Who's your crush?")
  #make flower() (this is gonna be just the flower head lol.)
  #make petals() (function should have random generated and the petals should be either clicked or spacebar to pop off.)


#def make_petals():
  


'''

def petalclicked():
  text on screen switch from "they love me, they love me not" (modulus operator my behated lol)

def IM GONNA KILL MYSELF IM GONNA KILL MYSELF IM GONNA KILL MYSEL

'''
#-----events----------------

#startgame()
#wn.onkeypress(make_petals,"f")
wn.listen
wn.mainloop()
