import tkinter as tk  # 載入 tkinter 模組

window = tk.Tk()   # 建立主視窗

window.title("button")  # 視窗名稱

window.geometry("320x240") # 視窗大小

var = tk.StringVar()

label = tk.Label(textvariable=var, background="orange", font=("Arial",12), width=15, height=2)

label.pack()

on_click = False

def click_me():
    global on_click
    if on_click == False:
        on_click = True
        var.set("You click me")
    else:
        on_click = False
        var.set("")

btn = tk.Button(text="Click me", width=30, height=2, command=click_me)

btn.pack()

window.mainloop()