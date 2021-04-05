import tkinter as tk

window = tk.Tk()

window.title("Radiobutton")

window.geometry("300x200")

window.config(bg="black")

var = tk.StringVar()
lb = tk.Label(bg="white", width=20, text="")
lb.pack()

def print_selection():
    lb.config(text="You have selected " + var.get())


r1 = tk.Radiobutton(text="OptionA", variable=var, value="A", command=print_selection)
r1.pack()

r2 = tk.Radiobutton(text="OptionB", variable=var, value="B", command=print_selection)
r2.pack()

r3 = tk.Radiobutton(text="OptionC", variable=var, value="C", command=print_selection)
r3.pack()


window.mainloop()