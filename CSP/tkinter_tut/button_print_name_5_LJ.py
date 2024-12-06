import tkinter

root = tkinter.Tk()

def printName():
  print("Hello my name is ")

def awoo():
  label_1= tkinter.Label(root, text="AWOOOOO!!!")
  label_1.pack()

button_1= tkinter.Button(root, text="Can we get an Awoo in chat?",command= awoo)
#binding function to a widget
button_1.pack()

root.mainloop()