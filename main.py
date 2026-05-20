import random as rm

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
    length = int(input("Input required password length"))
    password = ""
    for i in range(length):
        random_character = rm.choice(characters)
        password = password + random_character

    print("Generated password: ", password)

#--------------Menu------------------
print("1. Check Password")
print("2. Generate Password")
choice = input("choose an option: ")

#-------------Function selector------------------------------------------
if choice == "1":
    password_check()
elif choice =="2":
    password_generator()
else:
    print("Invalid option selected")

print("==========================================================")
print("====================Complete==============================")
print("==========================================================")
