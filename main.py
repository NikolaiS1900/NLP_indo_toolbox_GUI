import tkinter as tk
from gui_handler import GUI_handler

def main():
    """Initialize and run the GUI application."""
    root = tk.Tk()  # Create the root window
    app = GUI_handler(root)  # Pass the root window to your GUI_handler class
    root.mainloop()  # Start the main event loop

if __name__ == "__main__":
    main()  # Execute the main function if this file is run directly
