import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Checkbox GUI Example")
        self.root.geometry("900x700")

        # Define a dictionary to keep track of checkbox states
        self.checkbox_vars = {
            "Option 1": tk.BooleanVar(),
            "Option 2": tk.BooleanVar(),
            "Option 3": tk.BooleanVar(),
            "Option 4": tk.BooleanVar(),
        }

        # Define a dictionary for nested checkboxes under "Option 2"
        self.nested_checkbox_vars = {
            "Nested Option 1": tk.BooleanVar(),
            "Nested Option 2": tk.BooleanVar(),
            "Nested Option 3": tk.BooleanVar(),
        }

        # Create the checkboxes
        self.create_checkboxes()

    def create_checkboxes(self):
        # Frame for main checkboxes
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(anchor="w", fill="x", expand=True)

        # Loop through the dictionary and create a checkbox for each item
        for text, var in self.checkbox_vars.items():
            checkbox = ttk.Checkbutton(
                main_frame,
                text=text,
                variable=var,
                command=lambda t=text: self.on_checkbox_toggle(t)
            )
            checkbox.pack(anchor="w")

            # If it's "Option 2", create nested checkboxes
            if text == "Option 2":
                # Frame for nested checkboxes
                nested_frame = ttk.Frame(main_frame, padding=20)
                nested_frame.pack(anchor="w", fill="x", padx=20)

                for nested_text, nested_var in self.nested_checkbox_vars.items():
                    nested_checkbox = ttk.Checkbutton(
                        nested_frame,
                        text=nested_text,
                        variable=nested_var,
                        command=lambda nt=nested_text: self.on_nested_checkbox_toggle(nt)
                    )
                    nested_checkbox.pack(anchor="w")

    def on_checkbox_toggle(self, option):
        # Check the state of the main checkbox and call the corresponding method
        if self.checkbox_vars[option].get():
            self.show_message(f"{option} is selected", "Info")
            self.perform_action(option)
        else:
            self.show_message(f"{option} is deselected", "Info")
            self.stop_action(option)

    def on_nested_checkbox_toggle(self, nested_option):
        # Check the state of the nested checkbox and call the corresponding method
        if self.nested_checkbox_vars[nested_option].get():
            self.show_message(f"{nested_option} is selected", "Info")
            self.perform_action(nested_option)
        else:
            self.show_message(f"{nested_option} is deselected", "Info")
            self.stop_action(nested_option)

    def show_message(self, message, title):
        # Display a message box with the given message and title
        messagebox.showinfo(title, message)

    def perform_action(self, option):
        # Example method to perform an action when a checkbox is selected
        print(f"Performing action for {option}")

    def stop_action(self, option):
        # Example method to stop an action when a checkbox is deselected
        print(f"Stopping action for {option}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
