import tkinter as tk  # 載入 tkinter 模組

window = tk.Tk()   # 建立主視窗

window.title("button")  # 視窗名稱

window.geometry("800x600") # 視窗大小

def click():
    print("Pika Pika chu ~~~")

# Image
img = tk.PhotoImage(file="E:/Python-learning/Tkinter-GUI/picture/Pikachu.png")


# Button
btn = tk.Button(image=img, command=click)

btn.pack()

window.mainloop()