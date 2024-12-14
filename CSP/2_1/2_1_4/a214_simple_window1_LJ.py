#   a214_simple_window1_LJ.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x100")
root.title('Authorization')

frame_login = tk.Frame(root)
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

root.mainloop()