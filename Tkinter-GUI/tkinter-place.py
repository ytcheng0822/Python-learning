import tkinter as tk

win = tk.Tk()

win.title("pack & place布局")

win.geometry("300x300")

# pack佈局  (順序會影響佈局的方式)
# btn = tk.Button(text="Button")
# btn.pack(side="top")
# btn = tk.Button(text="Button")
# btn.pack(side="bottom")
# btn = tk.Button(text="Button")
# btn.pack(side="left")
# btn = tk.Button(text="Button")
# btn.pack(side="right")


# place佈局
btn = tk.Button(text="Button")
btn.place(anchor="center", x=150, y=150, width=100, height=50)  # anchor 元件的原點位置


win.mainloop()