import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()

window.title("Login")

window.geometry("1000x600")


# welcome image

canvas = tk.Canvas(window, width=900, height=300)
image_file = tk.PhotoImage(file="E:/Python-learning/Tkinter-GUI/picture/user.png")
image = canvas.create_image(265,90,anchor="nw",image=image_file)
canvas.pack(side="top")


# user information
user = tk.Label(window, text="User name:")
user.config(font=("Arial",15), width=15, height=2)
user.place(x=250,y=300)

password = tk.Label(window, text="Password:")
password.config(font=("Arial",15), width=15, height=2)
password.place(x=250,y=350)


# entry
var_user_name = tk.StringVar()
var_user_name.set("example@python.com")
var_password = tk.StringVar()

user_entry = tk.Entry(window, textvariable=var_user_name, font=("Arial",15))
user_entry.place(x=400,y=314)

password_entry = tk.Entry(window, textvariable=var_password, show="*", font=("Arial",15))
password_entry.place(x=400,y=364)


def user_login():
    user_name = var_user_name.get()
    password = var_password.get()
    try:
        with open("users_info.pickle","rb") as user_file:
            users_info = pickle.load(user_file)
    
    except FileNotFoundError:
        with open("users_info.pickle","wb") as user_file:
            users_info = {"admin":"admin"}
            pickle.dump(users_info, user_file)
    if user_name in users_info:
        if password == users_info[user_name]:
            tk.messagebox.showinfo(title="Welcome", message="How are you?  " + user_name)
        else:
            tk.messagebox.showerror(title="Error", message="Your password is wrong, please try again !!")
    else:
        is_sign_up = tk.messagebox.askyesno("Sign up", "You have not sign up yet. Sign up now?")     
        if is_sign_up:
            user_sign_up()

def user_sign_up():
    def sign_to_Login():
        nn = new_name.get()
        np = new_password.get()
        npc = new_password_confirm.get()
        with open("users_info.pickle","rb") as user_file:
            exist_user_info = pickle.load(user_file)
        
        if np != npc:
            tk.messagebox.showerror(title="Error", message="Password and confirm password must be the same!")
        
        elif nn in exist_user_info:
            tk.messagebox.showerror(title="Error", message="The user has already signed up!")
        
        else:
            exist_user_info[nn] = np
            with open("users_info.pickle","wb") as user_file:
                pickle.dump(exist_user_info, user_file)
            tk.messagebox.showinfo("Welcome", "You have successfully signed up!")
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)  # 視窗上的視窗
    window_sign_up.geometry("380x400")
    window_sign_up.title("Sign up")

    new_name = tk.StringVar()
    new_name.set("example@python.com")
    tk.Label(window_sign_up, text="User name:").place(x=80,y=50)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150,y=50)

    new_password = tk.StringVar()
    tk.Label(window_sign_up, text="Password:").place(x=85,y=90)
    entry_user_password = tk.Entry(window_sign_up, textvariable=new_password, show="*")
    entry_user_password.place(x=150,y=90)

    new_password_confirm = tk.StringVar()
    tk.Label(window_sign_up, text="Confirm password:").place(x=35,y=130)
    entry_user_password_confirm = tk.Entry(window_sign_up, textvariable=new_password_confirm, show="*")
    entry_user_password_confirm.place(x=150, y=130)

    btn_confirm_sign_up = tk.Button(window_sign_up, text="Sign up", command=sign_to_Login)
    btn_confirm_sign_up.place(x=150, y=180)


# login and sign up button
btn_login = tk.Button(window, text="Login", command=user_login)
btn_login.config(width=8,height=2)
btn_login.place(x=400,y=415)

btn_sign_up = tk.Button(window, text="Sign up", command=user_sign_up)
btn_sign_up.config(width=8,height=2)
btn_sign_up.place(x=500,y=415)


window.mainloop()