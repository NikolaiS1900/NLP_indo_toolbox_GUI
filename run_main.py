import json
import re
import tkinter as tk
from info_window import open_new_window
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
        self.selected_language = None  # Instance variable for the selected language
        self.selected_search_type = None

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

        # Bind the "Enter" key to the perform_regex_search function
        self.user_input_entry.bind("<Return>", self.perform_regex_search)

        self.regex_search_button = ttk.Button(root, text="Regex Search", command=self.perform_regex_search)
        self.regex_search_button.pack(pady=10)

        # Create Combobox for language selection (initially hidden)
        self.language_dropdown = ttk.Combobox(root, values=[], state='readonly')
        self.language_dropdown.pack(pady=10)
        self.language_dropdown.pack_forget()  # Hide it initially

        # Dropdown for selecting search type
        self.search_type = ttk.Combobox(root, values=["Anlaut", "Inlaut", "Auslaut"], state='readonly')
        self.search_type.pack(pady=10)
        self.search_type.pack_forget()  # Hide it initially

    def mii(self):
        messagebox.showinfo(self.load_json_content("lang_pack/sound_category_dictionary.json"))

    def show_languages(self):
        """Show the language dropdown when the button is pressed."""
        # Populate the language dropdown
        self.language_options = list(self.languages_dict.keys())
        self.language_dropdown.config(values=self.language_options)
        
        # Show the language dropdown
        self.language_dropdown.pack()
        self.language_dropdown.set("Select regex overview")  # Default text
        
        # Bind event for language selection
        self.language_dropdown.bind("<<ComboboxSelected>>", self.on_language_selected)


    def on_language_selected(self, event):
        """Handle the event when a language is selected."""
        self.selected_language = self.language_dropdown.get()  # Store the selected language

        selected_language_dictionary = self.languages_dict[self.selected_language]

        dictionary_list = []

        for key, value in selected_language_dictionary.items():
            dictionary_list.append(f"ᚱ{key}ᚱ = {value}")

        dictionary_list_string = "\n\n".join(dictionary_list)

        # Call open_new_window immediately after a language is selected
        open_new_window(self.root, dictionary_list_string)

    def show_search_type(self):
        self.search_type.pack()
        self.search_type.set("Select Search Type")

        # Bind event for language selection
        self.search_type.bind("<<ComboboxSelected>>", self.on_search_type_selected)

    def on_search_type_selected(self, event):
        self.selected_search_type = self.search_type.get()

    def perform_regex_search(self, event=None):
        """Handle regex search when the button is pressed."""
        self.show_languages()
        self.show_search_type()

        # Show the user input field
        self.user_input_entry.pack()

        user_input_value = self.user_input.get()
        search_type_value = self.selected_search_type

        if user_input_value:
            messagebox.showinfo("Search Criteria", f"User Input: {user_input_value}"
                                f"\nSearch Type: {search_type_value}")
        else:
            pass


    def load_json_content(self, json_file_path):
        """Load the content of the specified JSON file."""
        if not json_file_path:
            raise ValueError(f"No JSON file path provided: {json_file_path}")

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
