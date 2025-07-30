import sys
from tkinter import *
root = Tk()
root.title("Python Text Editor")
label_test = Label(root, text="Welcome to my simple text editor!")
label_test.grid(row=0, column=0, pady=5)
text = Text(root, wrap='word')
text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()