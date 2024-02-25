Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import *

def btn_click():
    print("Button clicked")

    
window = Tk()
btn = Button(window, text="Click me!",command=btn_click)
btn.pack()

window.mainloop()
Button clicked
Button clicked
Button clicked
