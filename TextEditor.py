import sys
v = sys.version_info
content = None
if v.major == 2:
    print("Python Version 2.x") #for Version 2 of Python
    from tkinter import *
    import tkFileDialog as tkFileDialog
elif v.major == 3 and v.minor >= 4:
    print("Python Version 3.x")
    from tkinter import *
    import tkinter as tk
    from tkinter import filedialog as tkFileDialog, filedialog
else:
    print("Please, intall the Python 3.4 or higher versions!!!")
    sys.close()

def saveas():
    print("Saving as...")
    content = text_field.get("1.0", "end-1c")
    file = filedialog.asksaveasfile(
        mode="w",
        defaultextension=".txt",
        filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("HTML Files", "*.html"),("All files", "*.*"))
    )
    if file:
        try:
            file.write(content)
            file.close()
            print(f'File object closed, DEBUG: {content}')
            print("Filed saved!")
        except Exception as e:
            print(f'ERROR, could not save file: {e}')
        else:
            print(f'File saved successfully!')

print("Running....")
root = tk.Tk()
root.configure(background="#17313E")
root.title("Text Editor")
root.grid()
label_subtitle = tk.Label(root, text="Welcome, here you can write text and scripts for your programs!", padx=5, background="#3e4451", font=("Arial", 10), fg="#C5B0CD")
label_subtitle.grid(row=0, column=0, padx=10, pady=10)
text_field = Text(root, wrap=WORD, background="#415E72", fg="#C5B0CD", font=("Arial", 15, "bold"))
text_field.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
text_field.insert("1.0", "Insert your code here")
button = tk.Button(root, text="Save as", command=saveas, background="#F3E2D4", fg="black")
button.grid(row=1, column=0, padx=5, pady=10)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()