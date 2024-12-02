import tkinter

root = tkinter.Tk()

def printName():
  print("Hello my name is Lucille")

button_1= tkinter.Button(root, text="Print my name",command= printName)
#binding function to a widget
button_1.pack()

root.mainloop()