#   a114_while_guess.py
import turtle as trtl
import random


# modify with colors
rcolor = ["cyan", "darkorchid", "navy", "deepskyblue", "orchid", "violet", "darkblue", "navy", "indigo","blue","mediumslateblue","mediumpurple", "blueviolet","darkviolet","royalblue","mediumblue","midnightblue"]
wn = trtl.Screen()




color = random.choice(rcolor)
painter = trtl.Turtle()
painter.shape("circle")


w = 3
painter.width(1.5)
painter.speed(0)
painter.color(color)


painter = trtl.Turtle()
space = 1
angle = 180 # experiment with the shape
count = 0
radius = 30
def draw_star(painter, x, y):
    painter.speed(0)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
    painter.color("gold")
    painter.begin_fill()
    for _ in range(5):
        painter.forward(10)
        painter.right(144)
    painter.end_fill()


# Draw multiple stars
for _ in range(7):
    draw_star(painter, random.randint(-200, 200), random.randint(-200, 200))
    


for lines in range (4):
  color = random.choice(rcolor)
  w = 1
  painter.speed(0)
  painter.color(color)
  painter.penup()
  painter.goto(0,0)
  painter.pendown()
  painter.right(75)
  space = 1
  angle = 180 # experiment with the shape
  count = 0
  while (count < 50):
    color = random.choice(rcolor)
    painter.color(color)
    w = w + 0.15
    painter.width(3)
    painter.right(angle)
    painter.penup()
    painter.forward(space) # experiment
    painter.pendown()
    painter.begin_fill()
    painter.circle(w)
    painter.end_fill()
    space += 6
    angle = angle + 0.05
    count = count + 1
  count = 0




#star qualities
painter.shape("classic")
painter.penup()
painter.goto(-100, 100)
painter.pendown()
painter.color("lemonchiffon")
painter.begin_fill()
y = 100
x = -100


#amt of stars
for line in range (4):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
  painter.begin_fill()
  
  #make each star
  for i in range(5):
    painter.color("gold")
    painter.forward(40)
    painter.right(144)


  painter.end_fill()
  painter.penup()


  if (x < 100):
    x = 100
  elif (x >= 100):
    x = -100
  y = y - 70 


wn.mainloop()
