#   a118_grades.py
#   This code is incomplete. 
my_courses = ["English", "Math", "CS"]

redo = "y"

while (redo == "y"):
  for course in my_courses:
    print("Enter your points for " + course)
    points = int(input("Points ->"))
    if (points >= 90):
      print("A")
    elif (points >= 80):
      print("B")
    elif (points >= 70):
      print("C")
    elif (points >= 60):
      print("D")
    else:
      print("F")
  redo = input("Do you need to re-do these grades? (y/n)")



# pseudocode :3
'''set variable redo Y
loop (runs while redo==Y)
  for course in my_courses:
    print() # blank line
    print("Enter your points for " + course)
    points = int(input("Points -> "))

    if (points >= 90):
      print("A")
    elif (points >= 80):
      print("B")
    elif (points >= 70):
      print("C")
    elif (points >= 60):
      print("D")
    else:
      print("F")
  redo = input("Do you need to re-do these grades? (y/n)")

'''