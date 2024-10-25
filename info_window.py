import tkinter as tk
from tkinter import Toplevel


def open_new_window(root, info_text):
    """
    Creates a new Toplevel window to display the given information.
    
    Args:
        root (tk.Tk): The main Tkinter root window.
        info_text (str): The text to display in the new window.
    """
    new_window = tk.Toplevel(root)
    new_window.title("Copy and paste regex short cuts")
    new_window.geometry("400x600")  # Adjust size as needed

    # Create a Text widget to display the information
    text_widget = tk.Text(new_window, wrap="word", height=15, width=50)
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)

    # Insert the info_text into the Text widget
    text_widget.insert(tk.END, info_text)

    # Make the Text widget read-only
    text_widget.config(state="disabled")

    # Create a Scrollbar for the Text widget
    # Add a scrollbar for longer content
    scrollbar = tk.Scrollbar(new_window, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
