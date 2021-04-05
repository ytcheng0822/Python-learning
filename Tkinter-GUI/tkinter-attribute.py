# 標題, 大小, icon, 顏色, 透明度, 置頂

import tkinter as tk

window = tk.Tk()

# 標題
window.title("attribute")

# 大小
window.geometry("400x200")  # 寬x高
# window.minsize(width=400, height=200)
# window.maxsize(width=1024, height=768)
window.resizable(False, False)   # 固定視窗大小

# icon
window.iconbitmap("E:/Python-learning/Tkinter-GUI/picture/github-512.ico")  # .ico

# 顏色
window.config(background="skyblue")

# 透明度
window.attributes("-alpha", 0.686)  # 1~0  1=100%  0=0%

# 置頂
window.attributes("-topmost", True)


window.mainloop()