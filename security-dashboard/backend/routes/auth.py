# This file is for user authentication signup and login.
# How it should work user sends username, email, and password.
# Needs to ask the user for those things.
# Check if username is taken.
# If not taken hash the password and save user in database(not setup atm just ref it).
# Return success message.

import bcrypt

users_db = {}

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def signup():
    username = input("Enter a username: ")
    if username in users_db:
        print ("Username is taken! Choose a different one. ")
        return

    email = input("Enter your email: ")
    password = input("Enter a password: ")

    # Hash the password before saving it
    hashed_password = hash_password(password)

    # Store user data (simulating database)
    users_db[username] = {"email": email, "password": hashed_password}
    print ("Signup successful! You can now login!")

    def verify_password(stored_password, entered_password):
        return bcrypt.checkpw(entered_password.encode(), stored_password)

def login():
    username = input("Enter your username: ")

    if username not in users_db:
        print("User not found! Please sign up first.")
        return False

    password = input("Enter your password: ")

    if verify_password(users_db[username]["password"], password):
        print("Login successful! Welcome,", username)
        return True
    else:
        print("Incorrect password! Try again.")
        return False

current_user = None  # Keeps track of the logged-in user

def dashboard():
    if current_user:
        print(f"Welcome to your dashboard, {current_user}!")
    else:
        print("Access Denied! Please log in first.")

def main():
    global current_user  # Allows modification of current_user inside functions
    
    while True:
        print("\nOptions: 1) Sign Up  2) Login  3) Dashboard  4) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            if login():
                current_user = input("Enter your username again to confirm: ")  # Store logged-in user
        elif choice == "3":
            dashboard()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


