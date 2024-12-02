import tkinter

root = tkinter.Tk() #creates window. root is to wn as tkinter.tk is to turtl.screen

one = tkinter.Label(root, text="One", bg="red", fg="white")
#creating a label named one, with a different background (fg) color and foreground (fg) or text color.
one.pack() #displays it in the window

two = tkinter.Label(root, text="Two", bg="green", fg="black")
two.pack(fill=tkinter.X) #we are specifying this label to be as long as the x value of the parent window is
#so the label wil grow when the window is stretched

three = tkinter.Label(root, text="Three", bg="blue", fg="white")
three.pack(side=tkinter.LEFT, fill=tkinter.Y)#throws label on the left hand side, and will stretch along the y of the window, filling it vertically

root.mainloop()