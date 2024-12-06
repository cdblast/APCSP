# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

#The username and password must each be at least eight characters long and no more than twenty-four characters long.
#The password must contain both letters and numbers.

usern = "n/a" #username 
passwrd = "n" #set both username and password to fail
requirements_met = False
while not requirements_met:
  usern = input("Set a username:")
  passwrd = input("Set a password:")
  if (len(usern) < 24 and len(usern) > 8) and (not passwrd.isalpha() and not passwrd.isdigit()): #both conditions met
    requirements_met = True 
  else: #at least one condition is failed, loop til strong passwrd and usern
    print("Try again. Hint: the password should combine BOTH numbers and letters. the username should be larger than 8 letters, but smaller than 24 letters.")


#my_auth.set_authorization("administrator3","1StrongPassword4CSP")
my_auth.set_authorization(usern,passwrd)

# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
