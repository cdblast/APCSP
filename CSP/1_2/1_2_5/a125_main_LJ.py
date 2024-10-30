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
'''
  maybe create petal_timesclicked to help w/ even/odd decider
'''
#-----initialize turtle-----
rands = rand.Random()

turtl = trtl.Turtle()

wn = trtl.Screen()
wn.bgcolor("white smoke")

#-----game functions--------
'''
def make_petals():
  sprites loaded in
  maybe do something like spawn in, rotate(divided by random petal amount decided) and go forward if spawning at origin fucks me in the ass lol.

def startgame():
  user input "Who's your crush?"
  make flower() (this is gonna be just the flower head lol.)
  make petals() (function should have random generated and the petals should be either clicked or spacebar to pop off.)

def petalclicked():
  text on screen switch from "they love me, they love me not" (modulus operator my behated lol)

def IM GONNA KILL MYSELF IM GONNA KILL MYSELF IM GONNA KILL MYSEL

'''
#-----events----------------

#startgame()
wn.mainloop()
