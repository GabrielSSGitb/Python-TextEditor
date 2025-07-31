import sys
from tkinter import *
v = sys.version_info #try to verify the py version here!!!
import tkinter as tk
from tkinter import filedialog
def saveas():
    global text_widget #Get the text on the field
    print("Save things here!!!")
def initialize():
    root = Tk()
    root.title("Python Text Editor")
    label_test = Label(root, text="Text Editor")
    label_test.grid(row=0, column=0, pady=5)
    text = Text(root, wrap='word')
    text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    button = tk.Button(text="Save As", command=saveas)
    button.grid()
    root.mainloop()
if v.major == 2:
    print("Python v2") #for Python v2 version
    from tkinter import *
    import tkFileDialog as tkFileDialog
    initialize()
elif v.major >= 3:
    initialize() # for Python v3
else:
    print("Unsupported version, please install the Python 3.4 or higher")
    sys.exit()