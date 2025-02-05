#   a214_simple_window1_LJ.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.scrolledtext as tksc

def test_my_button():
    frame_auth.tkraise()
    usr_pwd_lbl = tk.Label(frame_auth, text=ent_password.get(), font="Courier")
    usr_pwd_lbl.pack()

# main window
root = tk.Tk()
root.wm_geometry("200x150")
root.title('Authorization')

frame_login = tk.Frame(root)
frame_login.grid(row=0,column=0,sticky="news")

lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack(padx=50)
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack(padx=50)
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

bt_image = tk.PhotoImage(file="button.gif")
bt_image = bt_image.subsample(10,10)
button = tk.Button(frame_login, text = "Login", image=bt_image, command=test_my_button)
button.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0,column=0,sticky="news")

frame_login.tkraise()
test_textbox = tksc.ScrolledText(frame_auth)
test_textbox.configure(height=10, width=50)
test_textbox.pack(padx=50)

root.mainloop()