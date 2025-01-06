# a121_catch_a_turtle_LJ.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")
leader_names_list = []
leader_scores_list = []

colors = ["black", "teal", "pink", "orange", "purple", "red"]
font_setup = ("Arial", 20, "normal")
sizes = [0.5, 1, 1.5, 2, 2.5, 3]

trtl.addshape("milkbone.gif")
trtl.addshape("milkbonelight.gif")

turtl_shapesize = 2
turtl_shape = "milkbone.gif"
turtle_lightshape = "milkbonelight.gif"
turtl_color = "midnightblue"

timer = 5
counter_interval = 1000
timer_up = False
score = 0


#-----initialize turtle-----
rands = rand.Random()

turtl = trtl.Turtle()
turtl.shape(turtl_shape)
turtl.shapesize(turtl_shapesize)
turtl.fillcolor(turtl_color)

score_writer = trtl.Turtle()
counter = trtl.Turtle()
# counter.showturtle()

wn = trtl.Screen()
wn.bgcolor("white smoke")
#-----game functions--------

def turtl_clicked(x,y):
    #print("Turtl was clicked!")
    change_position()
    global timer_up
    if (not timer_up):
       update_score()
       addcolor()
       change_position()
       #resize()
    else:
       turtl.hideturtle()

def change_position():
    new_xpos = rand.randint(-250,250) #the limits are (400,300) but my screens too tiny! <3
    new_ypos = rand.randint(-150,150)
    turtl.penup()
    turtl.hideturtle()
    turtl.goto(new_xpos,new_ypos)
    turtl.pendown()
    turtl.showturtle()
    update_score()

def update_score():
  global score # gives this function access to the score that was created above
  score += 1
  score_writer.clear()
  score_writer.penup()
  score_writer.write("Score: " + str(score), font=font_setup)  
  # print(score)

score_writer.penup()
score_writer.goto(243, 225)
score_writer.pendown()
score_writer.hideturtle()

counter.penup()
counter.goto(-350,225)
counter.pendown()
counter.hideturtle()


#countdown function
def countdown():
   global timer, timer_up
   counter.clear()
   if timer <= 0:
      counter.write("Time's Up", font=font_setup)
      timer_up = True
      manage_leaderboard()
   else:
      counter.write("Timer: " +str(timer), font=font_setup)
      timer -= 1
      counter.getscreen().ontimer(countdown, counter_interval)

#addcolor function
def addcolor():
   turtl.shape(turtle_lightshape)
   turtl.stamp()
   turtl.shape(turtl_shape)

def resize():
   turtl.shapesize(rand.choice(sizes[0:]))

# start game function!!!
def start_game():
   turtl.onclick(turtl_clicked)
   counter.getscreen().ontimer(countdown, counter_interval)



def manage_leaderboard():
  global score
  global turtl
  global leader_names_list
  global leader_scores_list

  # get the names and scores from the leaderboard file
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  '''leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)
   '''
  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, turtl, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, turtl, score)

def leave_a_mark():
   turtl.shape(milkbonelight)
   turtl.stamp()
   turtl.fillcolor(colors[0]) #difficulty increased by commenting this out!


#-----events----------------
start_game()
wn.mainloop()
