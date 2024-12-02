import tkinter

root = tkinter.Tk()

label_1= tkinter.Label(root, text="First Name")
label_2= tkinter.Label(root, text="Password")

entry_1=tkinter.Entry(root)
entry_2=tkinter.Entry(root)

label_1.grid(row= 0, sticky=tkinter.E)
label_2.grid(row= 1, sticky=tkinter.E)

entry_1.grid(row= 0, column=1)
entry_2.grid(row= 1, column=1)

c = tkinter.Checkbutton(root, text="Keep me logged in")
c.grid(columnspan= 2)

root.mainloop()