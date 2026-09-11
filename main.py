import random as rm
import json
import sys
import os
import hashlib

if getattr(sys, 'frozen', False):
    # Running as a PyInstaller exe
    APP_DIR = os.path.dirname(sys.executable)
else:
    # Running as a normal .py script
    APP_DIR = os.path.dirname(os.path.abspath(__file__))

FILENAME = os.path.join(APP_DIR, "passwords.json")

#----------------------------------------------------------
#create master password
#----------------------------------------------------------
def setup_master_password():
    master_password = input("Enter your master passsword: ")
    password_bytes = master_password.encode()
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac(hash_name="sha256", password=password_bytes, salt=salt, iterations=100000, dklen=None)

    master_data = {
        "hash": hashed_password.hex(),
        "salt": salt.hex()
    }
    save_data("master.json", master_data)
    print("Master password set successfully.")

#---------------------------------------------------------
#verify master password
#---------------------------------------------------------
def verify_master_password():
    master_data = load_data("master.json")
    stored_hash = bytes.fromhex(master_data["hash"])
    salt = bytes.fromhex(master_data["salt"])
    master_password = input("Enter your master password to open the password manager: ")
    password_bytes = master_password.encode()
    hashed_password = hashlib.pbkdf2_hmac(hash_name="sha256", password=password_bytes, salt=salt, iterations=100000, dklen=None)

    if hashed_password == stored_hash:
        print("Opening password manager")
        return True
    else:
        print("Master password incorrect")
        return False

print("======================================")
print("=== Password checker and Generator ===")
print("======================================")

#------------------------Password checker---------------------------------
def password_check():
        print("checking password")
        user_password = input("Enter your password: ")
        required_length = int(input("Input required password length: "))
        special_characters = "!@#$%&*"
        has_special_characters = False
        numbers = "0123456789"
        has_numbers = False
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        has_uppercase_letters = False
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        has_lowercase_letters = False
        for character in special_characters:
            if character in user_password:
                has_special_characters = True
                break
        for num in numbers:
            if num in user_password:
                has_numbers = True
                break
        for uppercase in uppercase_letters:
            if uppercase in user_password:
                has_uppercase_letters = True
                break
        for lowercase in lowercase_letters:
            if lowercase in user_password:
                has_lowercase_letters = True
                break
        if len(user_password) >= required_length:
            print("Password is long enough")
        else:
            print("Password is not long enough")
        if has_special_characters and len(
                user_password) >= required_length and has_numbers and has_lowercase_letters and has_uppercase_letters:
            print("password is secure")
        else:
            print("password is weak")

#-------------------------password generator---------------------------------------------
def password_generator():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    length = int(input("Input required password length: "))
    password = ""
    for i in range(length):
        random_character = rm.choice(characters)
        password = password + random_character
    print("Generated password: ", password)
    return password

#-------------------------json load/save---------------------------------------------
def load_data(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

#-------------------------save a password entry---------------------------------------------
def save_password():
    data = load_data(FILENAME)
    service = input("Enter service/site name: ")
    password = input("Enter password to save (or leave blank to generate one): ")
    if password == "":
        password = password_generator()
    data[service] = password
    save_data(FILENAME, data)
    print(f"Password for {service} saved.")

#-------------------------view saved passwords---------------------------------------------
def view_passwords():
    data = load_data(FILENAME)
    if not data:
        print("No saved passwords yet.")
    else:
        for service, password in data.items():
            print(f"{service}: {password}")

if os.path.exists("master.json"):
    verify_master_password()
    access_granted = verify_master_password()
else:
    setup_master_password()
    access_granted = True

if access_granted:
#--------------Menu------------------
    while True:
        print("1. Check Password")
        print("2. Generate Password")
        print("3. Save Password")
        print("4. View Saved Passwords")
        print("5. Exit")
        choice = input("choose an option: ")

        #-------------Function selector------------------------------------------
        if choice == "1":
            password_check()
        elif choice == "2":
            password_generator()
        elif choice == "3":
            save_password()
        elif choice == "4":
            view_passwords()
        elif choice == "5":
            print("==========================================================")
            print("====================Complete==============================")
            print("==========================================================")
            break
        else:
            print("Invalid option selected")

    print("==========================================================")
