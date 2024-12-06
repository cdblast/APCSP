# debug_methods_LJ.py
#this isnt code, this is a "notebook" 
#to understand how to workaround bugged or improvable code.

'''
key = int(input("Enter the Encryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)
'''
#This will crash if it receives anything besides an integer.
#We can use .isdigit() to check if there is a digit,
#which then will let us proceed without crashing the program.
'''
noninteger = False
key = "word"
mod_value = "letter"
keyint = 0
mod_value = 0

while not noninteger:
  key = input("Enter the Encryption Key: " )
  mod_value = input("Enter the Modulus: " )
  if key.isdigit() and mod_value.isdigit():
    noninteger = True
    keyint = int(key)
    mod_valueint = int(mod_value)
  else: 
    print("Please provide integers.")

plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(keyint, mod_valueint, plaintext)
print("Encrypted Message:", encrypted_msg)
'''
#We can use .isalpha() the same to check if a string has ONLY letters.

#len(string) returns the length of a string :3
'''
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
'''