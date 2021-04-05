import tkinter as tk

window = tk.Tk()

window.title("Listbox")

window.geometry("400x200")

window.config(bg="black")

var1 = tk.StringVar()
label = tk.Label(bg="white",width=15, textvariable=var1)
label.pack()

def print_selection():
    value = listbox.get(listbox.curselection())
    var1.set(value)


btn = tk.Button(text="print selection", command=print_selection)
btn.pack()

var2 = tk.StringVar()
var2.set(("apple","banana","watermelon","orange"))
listbox = tk.Listbox(listvariable=var2)

listbox.insert(2,"cherry")
listbox.delete(4)
listbox.pack()

window.mainloop()