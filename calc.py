import tkinter
from tkinter.constants import *
window = tkinter.Tk() # 生成窗口对象
frame = tkinter.Frame(window, relief = RIDGE, borderwidth = 2)
frame.pack(fill = BOTH, expand = 1)
label = tkinter.Label(frame, text = "Hello, World")
label.pack(fill = X, expand = 1)
button = tkinter.Button(frame, text="Exit", command=window.destroy)
button.pack(side = BOTTOM)
button_new = tkinter.Button(frame, text = "New Window")
window.mainloop() # 需要这一句才能交互