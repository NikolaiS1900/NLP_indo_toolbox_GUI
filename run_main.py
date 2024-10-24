import json
import re
import tkinter as tk
from load_file import load_file
from load_json import load_json
from char_list import char_list
from preprocess import preprocess
from tkinter import messagebox, filedialog, ttk
from word_list import make_word_list

class App:
    """GUI Application for text processing."""

    def __init__(self, root):
        self.root = root
        self.root.title("Text Processing Application")
        self.root.geometry("600x500")

        self.user_input = tk.StringVar()
        self.file_path = tk.StringVar()

        # Load the dictionary from the JSON file
        self.languages_dict = self.load_json_content("lang_pack/sound_category_dictionary.json")

        # Create input for file path
        self.file_entry = tk.Entry(root, textvariable=self.file_path, width=40)
        self.file_entry.pack(pady=10)

        # Create a button for browsing a file
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        # Create buttons for processing
        self.char_button = tk.Button(root, text="Generate Character List", command=self.generate_char_list)
        self.char_button.pack(pady=10)

        self.preprocess_button = tk.Button(root, text="Preprocess Text", command=self.preprocess_text)
        self.preprocess_button.pack(pady=10)

        self.word_button = tk.Button(root, text="Generate Word List", command=self.generate_word_list)
        self.word_button.pack(pady=10)


        self.quit_button = tk.Button(root, text="Mii", command=self.mii)
        self.quit_button.pack(pady=10)


    # Create a text input field for user input
        self.user_input_entry = tk.Entry(root, textvariable=self.user_input, width=40)
        self.user_input_entry.pack(pady=10)
        self.user_input_entry.pack_forget()  # Hide it initially

        self.anlaut_button = ttk.Button(root, text="Anlaut", command=self.anlaut_button)
        self.anlaut_button.pack(pady=10)


       # Create a button to show the language dropdown
        self.show_languages_button = ttk.Button(root, text="Select Language", command=self.show_languages)
        self.show_languages_button.pack(pady=10)
        self.show_languages_button.pack_forget()  # Hide it initially

        # Create Combobox for language selection (initially hidden)
        self.language_dropdown = ttk.Combobox(root, values=[], state='readonly')
        self.language_dropdown.pack(pady=10)
        self.language_dropdown.pack_forget()  # Hide it initially



    def mii(self):
        messagebox.showinfo(self.load_json_content("lang_pack/sound_category_dictionary.json"))




    def show_languages(self):
        """Show the language dropdown when the button is pressed."""
        # Populate the language dropdown
        self.language_options = list(self.languages_dict.keys())
        self.language_dropdown.config(values=self.language_options)
        
        # Show the language dropdown
        self.language_dropdown.pack()
        self.language_dropdown.set("Select a language")  # Default text
        
        # Bind event for language selection
        self.language_dropdown.bind("<<ComboboxSelected>>", self.on_language_selected)



    def on_language_selected(self, event):
        """Handle the event when a language is selected."""
        selected_language = self.language_dropdown.get()
        print(f"Selected language: {selected_language}")

        # Populate the key dropdown with keys from the selected language
        language_data = self.languages_dict.get(selected_language, {})
        self.key_options = list(language_data.keys())
        
        # Show the the user input field
        self.user_input_entry.pack()
        
        # Bind event for key selection
        self.user_input_entry.bind("<<ComboboxSelected>>", self.anlaut_button)


    def anlaut_button(self, event=None):
        """Display the language dropdown when the Anlaut button is pressed."""
        self.show_languages()

    def load_json_content(self, json_file_path):
        """Load the content of the specified JSON file."""

        if not json_file_path:
            raise ValueError(f"No JSON file path provided.{json_file_path}")

        return load_json(json_file_path)

    def browse_file(self):
        """Open a file dialog to select a file."""
        file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_path.set(file_path)

    def load_file_content(self, file_path):
        """Load the content of the specified file."""
        if not file_path:
            raise ValueError("No file path provided.")
        return load_file(file_path)

    def generate_char_list(self):
        """Handle character list generation."""
        try:
            text = self.load_file_content(self.file_path.get())

            list_of_characters = char_list(text)

            file_name = re.sub(r".*[\\/]", "", self.file_path.get())
            file_name_no_extension = file_name.replace(".txt", "")

            with open(f"preprocess/{file_name_no_extension}_characters_to_delete.txt",
                      "w", encoding="utf8") as output_file:
                output_file.write(list_of_characters)

            messagebox.showinfo("Success", "Character list has been saved in "
                                f"preprocess/{file_name_no_extension}_characters_to_delete.txt"
                                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def preprocess_text(self):
        """Handle text preprocessing."""
        try:
            # Open a new file selection dialog for preprocessing
            char_list = filedialog.askopenfilename(title="Select a Text File to Preprocess", filetypes=[("Text Files", "*.txt")])
            if not char_list:
                return  # If no file is selected, exit the method

            char_list = self.load_file_content(char_list)  # Load content from the selected file

            text = self.load_file_content(self.file_path.get())

            preprocessed_text = preprocess(text, char_list)

            file_name = re.sub(r".*[\\/]", "", self.file_path.get())
            file_name_no_extension = file_name.replace(".txt", "")

            with open(f"preprocess/{file_name_no_extension}_preprocessed.txt",
                      "w", encoding="utf8") as output_file:
                output_file.write(preprocessed_text)

            messagebox.showinfo("Success", f"{file_name} has been preprocessed and saved in"
                                f"preprocess/{file_name_no_extension}_preprocessed.txt.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_word_list(self):
        """Handle word list generation."""
        try:
            text = self.load_file_content(self.file_path.get())

            word_list = make_word_list(text)

            file_name = re.sub(r".*[\\/]", "", self.file_path.get())
            file_name_no_extension = file_name.replace(".txt", "")

            with open(f"{file_name_no_extension}_word_list.txt", "w",
                      encoding="utf8") as output_file:
                output_file.write(word_list)

            messagebox.showinfo("Success", "Word list has been saved in"
                                f"{file_name_no_extension}_word_list.txt.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def anlaut_search(self):
        """Show additional widgets based on the selection."""
        selected_language = self.language_dropdown.get()
        print(f"Selected language: {selected_language}")


if __name__ == "__main__":

    root = tk.Tk()
    app = App(root)
    root.mainloop()
