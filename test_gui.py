# interface.py
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class TkinterInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Example")
        self.root.geometry("300x300")
        
        # Dropdown options
        self.options1 = ["Option 1", "Option 2", "Option 3"]
        self.options2 = ["Choice A", "Choice B", "Choice C"]

        # Create Comboboxes (dropdown menus)
        self.dropdown1 = ttk.Combobox(root, values=self.options1)
        self.dropdown2 = ttk.Combobox(root, values=self.options2)

        # Create text entry field
        self.entry_field = tk.Entry(root)

        # Create a button to trigger the function
        self.show_button = ttk.Button(root, text="Show Widgets", command=self.show_widgets)
        self.show_button.pack(pady=20)

        # Create a button to browse a file
        self.browse_button = ttk.Button(root, text="Browse File", command=self.browse_file)
        self.browse_button.pack(pady=20)

    def show_widgets(self):
        """Show dropdown menus and text entry field."""
        # Dropdown menu 1
        dropdown1_label = ttk.Label(self.root, text="Select Option 1:")
        dropdown1_label.pack(pady=5)
        self.dropdown1.pack(pady=5)

        # Dropdown menu 2
        dropdown2_label = ttk.Label(self.root, text="Select Option 2:")
        dropdown2_label.pack(pady=5)
        self.dropdown2.pack(pady=5)

        # Text entry field
        entry_label = ttk.Label(self.root, text="Enter a string:")
        entry_label.pack(pady=5)
        self.entry_field.pack(pady=5)

    def browse_file(self):
        """Open a file dialog to select a file."""
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All Files", "*.*")])
        if file_path:
            # Display the selected file path or perform other actions
            print(f"Selected file: {file_path}")
