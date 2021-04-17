import tkinter as tk

win = tk.Tk()

win.title("Grid")

win.geometry("250x100")

# Grid 網格布局  (不能和pack一起使用)
user = tk.Label(text="User")
user.grid(row=0, column=0)


password = tk.Label(text="Password")
password.grid(row=1, column=0)


user_entry = tk.Entry()
user_entry.grid(row=0, column=1)

password_entry = tk.Entry()
password_entry.grid(row=1, column=1)



win.mainloop()