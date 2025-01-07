import tkinter as tk

root = tk.Tk()
root.wm_geometry("200x200")
root.title("Tk colorgrid")

blue_frame = tk.Frame(root, height=100, width=150, background="blue")
blue_frame.grid(column=0, row=0)

red_frame = tk.Frame(root, height=100, width=150, background="red")
red_frame.grid(column=0, row=1)

lime_frame = tk.Frame(root, height=100, width=50, background="lime")
lime_frame.grid(column=1, row=0) 

yellow_frame = tk.Frame(root, height=100, width=50, background="yellow")
yellow_frame.grid(column=1, row=1) 

root.mainloop()