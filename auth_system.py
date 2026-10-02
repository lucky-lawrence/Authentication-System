import json
import hashlib
import getpass

def save_users():
    with open("users.json" , "w") as file:
        json.dump(users, file, indent = 4)

def load_users():
    with open ("users.json", "r") as file:
        return json.load(file)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    if not username:

        print("Username cannot be empty.")

        return

    if not password:

        print("Password cannot be empty.")

        return
    if len(password) < 8:
       print("Password must be at least 8 characters.")
       return
    
    for user in users:

        if user["username"].lower() == username.lower():

            print("Username already exists.")

            return
        
    hashed_password = hash_password(password)

    user = {
        "username": username,
        "password": hashed_password
    }
    users.append(user)
    save_users()
    print("Account created successfully!")


def login_user():
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    hashed_password = hash_password(password)

    for user in users:
        if user["username"].lower() == username.lower() and user["password"] == hashed_password:
            print("Login successful!")
            return user["username"]
    print("Invalid username or password.")
    return None   

def show_auth_menu():
    print("\n========================")
    print("   AUTHENTICATION SYSTEM")
    print("========================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("========================")

def show_user_menu(username):
    print("\n========================")
    print(f"Welcome, {username}!")
    print("========================")
    print("1. Logout")
    print("========================")    

users = load_users()

while True:
    show_auth_menu()

    choice = input("Choose an option: ").strip()

    if choice == "1":
        register_user()

    elif choice == "2":
        username = login_user()
        if username:

            while True:
                show_user_menu(username)

                user_choice = input("Choose an option: ").strip()

                if user_choice == "1":
                    print("Logged out successfully.")
                    break

                else:
                    print("Invalid option.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-3.")