#   a212_rsa_decrypt.py
import rsa as rsa

key = int(input("Enter the Decryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
'''
#improved code below
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
'''
encrypted_msg = input("What message would you like to decrypt (No brackets): ")
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))