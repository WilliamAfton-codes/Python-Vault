from cryptography.fernet import Fernet
import os
import sys
import time

print("Welcome to Python-Vault! (This is the DECRYPTER)\nMade with <3 by WilliamAfton-codes\n")
time.sleep(1)

current_script = sys.argv[0]

print(current_script)

files = []

directory = os.getcwd()

key = input("Paste in your Base64 key (DO NOT INCLUDE b' '): ").encode()

input("ALL FILES IN THIS DIRECTORY (except .py files) WILL BE DECRYPTED\nTHIS INCLUDES NON-ENCRYPTED FILES! \n\n[To proceed, press Enter]\n[To cancel, press Alt+F4 or close the program]")

print("\nDecrypting files, please wait...\n")

time.sleep(1)

for file in os.listdir():
    if file[-3:] == ".py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as files_to_decrypt:
        contents = files_to_decrypt.read()
    contents_dec = Fernet(key).decrypt(contents)
    with open(file, "wb") as files_to_decrypt:
        files_to_decrypt.write(contents_dec)

input("All files decrypted! Press Enter to close.")
