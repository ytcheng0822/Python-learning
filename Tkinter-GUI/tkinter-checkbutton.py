import tkinter as tk

window = tk.Tk()

window.title("Checkbutton")

window.geometry("300x200+750+300")

lb = tk.Label(bg="skyblue",width=20,text="")
lb.pack()

var1=tk.IntVar()
var2=tk.IntVar()

def print_selection():
    if(var1.get()==1)&(var2.get()==0):
        lb.config(text="I love only Python")
    elif(var1.get()==0)&(var2.get()==1):
        lb.config(text="I love only C++")
    elif(var1.get()==1)&(var2.get()==1):
        lb.config(text="I love both")
    else:
        lb.config(text="I do not love either")


c1 = tk.Checkbutton(text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection)
c2 = tk.Checkbutton(text="C++", variable=var2, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2.pack()

window.mainloop()