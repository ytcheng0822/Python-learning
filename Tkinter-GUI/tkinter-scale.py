import tkinter as tk

window = tk.Tk()

window.title("Scale")

window.geometry("400x300+700+300")

def change(self):
    s_value = s.get()
    window.attributes("-alpha", s_value/100)   # 利用get到的value來改變視窗的透明度

s = tk.Scale(orient=tk.HORIZONTAL, width=100, length=200)  # HORIZONTAL 橫向

s.config(from_=10, to=100)

s.config(showvalue=True, tickinterval=10, resolution=10)  # tickinterval 間隔單位,  resolution 一次移動多少單位

s.config(label="Tkinter Slider")

s.config(command=change)

s.set(100)    # 設定起始位置在100

s.pack()


window.mainloop()