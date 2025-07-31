import sys
import tkinter as tk
from tkinter import filedialog, scrolledtext # Import scrolledtext for built-in scrollbar

# Global variable for the text widget
text_field = None
# Global variable for the StringVar associated with the OptionMenu
variable = None

def saveas():
    global text_field # Use text_field consistently

    if text_field is None:
        print("Error: Text widget has not been initialized. Cannot save.")
        return

    content = text_field.get("1.0", "end-1c")
    print(f"DEBUG: Content to save: '{content}'")

    file = filedialog.asksaveasfile(
        mode='w',
        defaultextension=".txt",
        filetypes=(
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("HTML Files", "*.html"),
            ("All Files", "*.*")
        )
    )

    if file:
        try:
            file.write(content)
            file.close()
            print(f"DEBUG: File saved successfully to: {file.name}") # Use file.name for path
            print("File saved!")
        except Exception as e:
            print(f'ERROR: Could not save file: {e}')
    else:
        print("Save operation cancelled.")

# --- Function to handle dropdown menu selections ---
def menu_selection_handler(*args): # *args captures the unused name, index, mode arguments
    global variable # Access the global variable
    selected_option = variable.get() # Get the currently selected value

    print(f"Menu option selected: {selected_option}")

    if selected_option == "Save as":
        saveas()
    elif selected_option == "Save":
        print("Save option selected. (Implementing 'Save' requires tracking current file path)")
    elif selected_option == "File":
        # This is often just a placeholder or could open a new file dialog
        print("File option selected (usually a parent menu item).")


# --- Main GUI Setup ---
def initialize():
    global text_field, variable # Declare global for text_field and variable

    root = tk.Tk()
    root.title("Text Editor")
    root.geometry("800x600") # Set an initial size for better appearance
    root.configure(background="#282c34") # Dark background for the window

    # --- Header Frame for Menu and Label ---
    header_frame = tk.Frame(root, bg="#282c34")
    # Place the header frame at the top, stretching horizontally
    header_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    # Make the main window's column expand to fill space
    root.grid_columnconfigure(0, weight=1)

    # --- Dropdown Menu (OptionMenu) ---
    menu_options = ["File", "Save", "Save as", "Open", "New File"] # Added more options for example
    variable = tk.StringVar(root) # Create a StringVar associated with the root window
    variable.set(menu_options[0]) # Set the default value to "File"

    # Link the StringVar to the handler function
    variable.trace_add("write", menu_selection_handler)

    dropmenu = tk.OptionMenu(header_frame, variable, *menu_options) # Parent is header_frame
    dropmenu.config(
        bg="#61afef", fg="#ffffff", activebackground="#528cb6",
        activeforeground="#ffffff", borderwidth=0, highlightthickness=0,
        font=("Helvetica", 10, "bold"), padx=10, pady=5, cursor="hand2"
    )
    # Use pack to place the dropdown menu on the LEFT side of the header_frame
    dropmenu.pack(side=tk.LEFT, padx=5, pady=5)

    # --- Subtitle Label ---
    label_subtitle = tk.Label(
        header_frame, # Parent is header_frame
        text="Welcome, here you can write text and scripts for your programs!",
        font=("Arial", 10),
        bg="#282c34", # Match header_frame background
        fg="#abb2bf" # Light gray for text
    )
    # Use pack to place the label to the right of the dropdown, and make it expand
    label_subtitle.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

    # --- Text Editor Area (using ScrolledText for built-in scrollbars) ---
    text_field = scrolledtext.ScrolledText(
        root,
        wrap=tk.WORD, # Use tk.WORD for word wrapping
        font=("Consolas", 12), # Monospace font for code editor feel
        bg="#3e4451", # Dark background for text area
        fg="#abb2bf", # Light gray text
        insertbackground="white", # White cursor
        selectbackground="#4b628b", # Dark blue for selection
        borderwidth=0,
        highlightthickness=0,
        padx=10,
        pady=10
    )
    # Place the text area in row 1, below the header frame
    text_field.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    text_field.insert("1.0", "Insert your code here")

    # --- Configure row and column weights for responsiveness ---
    # Row 1 (where the ScrolledText is) should expand vertically
    root.grid_rowconfigure(1, weight=1)
    # Column 0 (which contains the header_frame and text_field) should expand horizontally
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

# --- Python Version Check ---
v = sys.version_info
if v.major >= 3:
    print(f"Python v{v.major} detected. Initializing editor.")
    initialize()
else:
    print("Unsupported Python version. Please install Python 3.4 or higher versions!!!")
    sys.exit()