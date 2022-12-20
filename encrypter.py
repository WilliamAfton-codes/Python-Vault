from cryptography.fernet import Fernet
import os
import sys
import time

print("Welcome to Python-Vault! (This is the ENCRYPTER)\nMade with <3 by WilliamAfton-codes\n")
time.sleep(1)

current_script = sys.argv[0]

print(current_script)

files = []

directory = os.getcwd()

key = Fernet.generate_key()

print("SAVE THIS KEY SOMEWHERE SAFE!: " + str(key))

time.sleep(3)

input("ALL FILES IN THIS DIRECTORY (except .py files) WILL BE ENCRYPTED! \n\n[To proceed, press Enter]\n[To cancel, press Alt+F4 or close the program]")

print("\nEncrypting files, please wait...\n")

time.sleep(1)

for file in os.listdir():
    if file[-3:] == ".py":
        continue
    if os.path.isfile(file):
        files.append(file)
 
for file in files:
    with open(file, "rb") as files_to_encrypt:
        contents = files_to_encrypt.read()
    contents_enc = Fernet(key).encrypt(contents)
    with open(file, "wb") as files_to_encrypt:
        files_to_encrypt.write(contents_enc)

input("All files encrypted! Press Enter to close.")
