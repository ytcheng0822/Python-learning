import tkinter as tk  # 載入 tkinter 模組

window = tk.Tk()   # 建立主視窗

window.title("start")  # 視窗名稱

window.geometry("320x240") # 視窗大小

label = tk.Label(window, text="This is my first Tk window ^^", background="orange", font=("Arial",12), width=30, height=2)

label.pack()  # 放置物件

window.mainloop()  # 常駐主視窗