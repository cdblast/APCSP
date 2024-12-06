#   a212_rsa_encrypt_LJ.py
import rsa as rsa
'''
key = int(input("Enter the Encryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)
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