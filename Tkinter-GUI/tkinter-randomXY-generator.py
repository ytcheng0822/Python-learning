import tkinter as tk

import random     # 處理隨機數生成

import pyperclip  # 處理複製的功能

window = tk.Tk()

window.title("Random X,Y Generator")

window.geometry("400x220+700+300")   # 從螢幕左上角(0,0)  x向右移動700  y向下移動300

window.config(bg="#323232")

title_text = tk.Label(text="Random X,Y Generator", fg="skyblue", bg="#323232", font=15)
title_text.pack()

min_range = tk.Label(text="Min range", fg="white", bg="#323232")
min_range.pack()
min_entry = tk.Entry()
min_entry.pack()

max_range = tk.Label(text="Max range", fg="white", bg="#323232")
max_range.pack()
max_entry = tk.Entry()
max_entry.pack()

x_show = tk.Label(text="", fg="white", bg="#323232")
x_show.pack()
y_show = tk.Label(text="", fg="white", bg="#323232")
y_show.pack()

def gen_xy():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    x = str(random.randint(min_val, max_val))   # random.randint(min, max) 取得一個隨機數
    y = str(random.randint(min_val, max_val))   # random.randint(min, max) 取得一個隨機數
    x_show.config(text = "X : " + x)
    y_show.config(text = "Y : " + y)

def copy():
    pyperclip.copy(x_show.cget("text") + "\n" + y_show.cget("text"))


generatte_btn = tk.Button(text="Generate", command=gen_xy)
generatte_btn.pack()
copy_btn = tk.Button(text="Copy", command=copy)
copy_btn.pack()

window.mainloop()