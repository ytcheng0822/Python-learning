import tkinter as tk

win = tk.Tk()
win.title("entry")
win.geometry("400x200")
win.config(background="black")

def click_ok():
    t = entry.get()
    lb.config(text = t)

lb = tk.Label(text="Please input any text", background="black", fg="white")
lb.pack()

entry = tk.Entry()
entry.pack()

btn = tk.Button(text = "OK", command = click_ok)
btn.pack()

win.mainloop()