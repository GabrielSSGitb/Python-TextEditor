import sys
v = sys.version_info
content = None
if v.major == 2:
    print("Python Version 2.x")
    from tkinter import *
    import tkFileDialog as tkFileDialog
elif v.major == 3 and v.minor >= 4:
    print("Python Version 3.x")
    from tkinter import *
    import tkinter as tk
    from tkinter import filedialog as tkFileDialog
else:
    print("Please, intall the Python 3.4 or higher versions!!!")
    sys.close()

def saveas():
    print("Saving as...")
    content = text_field.get("1.0", "end-1c")
    print(content)

print("Running....")
root = tk.Tk()
root.title("Text Editor")
root.grid()
label_subtitle = tk.Label(root, text="Welcome to your simple script interface!", padx=5)
label_subtitle.grid(row=0, column=0)
text_field = tk.Entry()
text_field = Text(root, wrap=WORD)
text_field.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
text_field.insert("1.0", "Insert your code here")
button = tk.Button(root, text="Save as", command=saveas)
button.grid(row=1, column=0, padx=5)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()