import json 
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)
    
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def login_windows():
    users = load_users()
    username_result = {"user": None}

    login = tk.Tk()
    login.title("login")
    login.geometry("300x200")

    tk.Label(login, text="Username").pack(pady=5)
    username_entry = tk.Entry(login)
    username_entry.pack(pady=5)

    tk.Label(login, text="Password").pack(pady=5)
    password_entry = tk.Entry(login, show="*")
    password_entry.pack(pady=5)

    # failed to login
    def try_login():
        user = username_entry.get()
        pw = password_entry.get()
        if user in users and users[user] == pw:
            username_result["user"] = user
            login.destroy()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")
    
    # register
    def register():
        user = username_entry.get()
        pw = password_entry.get()
        if user in users:
            messagebox.showerror("Error", "User already exists")
        else:
            users[user] = pw
            save_users(users)  # ✅ Pass the full dictionary!
            messagebox.showinfo("Success", "User is now registered")

    tk.Button(login, text="Login", command=try_login).pack(pady=5)
    tk.Button(login, text="Register", command=register).pack(pady=5)

    login.mainloop()
    return username_result["user"]
