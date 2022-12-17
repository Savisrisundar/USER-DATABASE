
from tkinter import *


win = Tk()


win.geometry("650x250")


entry= Entry(win)
entry.insert(END, 'Enter any Text')
entry.pack()

win.mainloop()