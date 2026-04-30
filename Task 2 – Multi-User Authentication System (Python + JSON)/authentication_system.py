import json
import hashlib
import os
import re

FILE = "users.json"

# Load users
def load_users():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Save users
def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)

# Hash password
def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Email check
def valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

# Strong password
def strong_pass(p):
    return len(p) >= 6

# Register
def register():
    users = load_users()

    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    for u in users:
        if u["username"] == username:
            print("Username already exists")
            return

    if not valid_email(email):
        print("Invalid email")
        return

    if not strong_pass(password):
        print("Weak password")
        return

    users.append({
        "username": username,
        "email": email,
        "password": hash_pass(password)
    })

    save_users(users)
    print("Registered successfully")

# Login
def login():
    users = load_users()

    username = input("Username/Email: ")
    password = hash_pass(input("Password: "))

    for u in users:
        if (u["username"] == username or u["email"] == username) and u["password"] == password:
            print("Login Successful")
            return

    print("Invalid credentials")

# Menu
while True:
    print("\n1.Register 2.Login 3.Exit")
    ch = input("Choose: ")

    if ch == "1":
        register()
    elif ch == "2":
        login()
    elif ch == "3":
        break
    else:
        print("Invalid choice")