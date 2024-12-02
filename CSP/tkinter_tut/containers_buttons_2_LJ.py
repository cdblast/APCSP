import tkinter

root = tkinter.Tk()

topFrame = tkinter.Frame(root)
topFrame.pack()

bottomFrame = tkinter.Frame(root)
bottomFrame.pack(side=tkinter.BOTTOM)

button1 = tkinter.Button(topFrame, text="Button 1", fg="red")
button2 = tkinter.Button(topFrame, text="Button 2", fg="blue")
button3 = tkinter.Button(topFrame, text="Button 3", fg="green")
button4 = tkinter.Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.LEFT)
button3.pack(side=tkinter.LEFT)
button4.pack(side=tkinter.BOTTOM)

root.mainloop()