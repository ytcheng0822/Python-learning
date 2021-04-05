import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.title("Messagebox")

window.geometry("300x200+750+300")

def click_me():
    tk.messagebox.showinfo(title="Hi", message="information")
    # tk.messagebox.showwarning(title="warning", message="Warning")
    # tk.messagebox.showerror(title="error", message="Error")
    # print(tk.messagebox.askquestion(title="Q&A", message="Yes or No"))   # return yes or no
    # print(tk.messagebox.askyesno(title="Q&A", message="True or False"))  # return True or False
    # print(tk.messagebox.askretrycancel(title="Q&A", message="True or False"))  # return True or False
    # print(tk.messagebox.askokcancel(title="Q&A", message="True or False"))     # return True or False

btn = tk.Button(text="click me", command=click_me)
btn.pack()


window.mainloop()