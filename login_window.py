import json 
import tkinter as tk
from tkinter import simpledialog, messagebox

USERS_FILE = "users.jason"

def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)
    
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def login_window():
    users = load_users()

    login = tk.Tk()
    login.title("login")
    login.geometry("300x200")

    tk.Label(login, text="Username").pack(pady=5)
    username_entry = tk.Entry(login)
    username_entry.pack(pady=5)

    tk.Label(login, text="Password").pack(pady=5)
    password_entry = tk.Entry(login, show="#")
    password_entry.pack(pady=5)

    # failed to login
    def try_login():
        user = username_entry.get()
        pw = password_entry.get()
        if user in users and users[user] == pw:
            login.destroy()
            return user
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")
    
    # register
    def register():
        user = username_entry.get()
        pw = password_entry.get()
        if user in users:
            messagebox.showerror("Error", "User already exists")
        else:
            save_users(user)
            messagebox.showinfo("Success", "User is now registered")
    tk.Button(login, text="login", command=lambda: login.quit()).pack(pady=5)
    tk.Button(login, text="login", command=register).pack()

    login.mainloop()
    return username_entry.get()
