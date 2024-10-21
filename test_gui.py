import tkinter as tk
from tkinter import messagebox, filedialog
from char_list import char_list
from load_file import load_file
from mk_text_dir import handle_text_dir
from preprocess import preprocess
from word_list import make_word_list

class Main:
    """Class for running the methods."""

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.text = self.load_text()

    def load_text(self):
        """Load text from the provided file path."""
        if self.file_path:
            try:
                return load_file(self.file_path)
            except Exception as e:
                raise ValueError(f"Error loading file: {str(e)}")
        else:
            raise ValueError("No file path provided.")

    def get_char_list(self) -> None:
        """Creates text file with the character list."""
        handle_text_dir("preprocess")

        list_of_characters = char_list(self.text)

        with open("preprocess/character_to_delete.txt", "w", encoding="utf8") as output_file:
            output_file.write(list_of_characters)

        message = (
            "\nYour character list is ready and has been saved in character_to_delete.txt.\n"
            "It is stored in the preprocess folder.\n"
            "Delete the characters you want to be removed from your text file."
        )

        return message

    def get_preprocessed_text(self) -> None:
        """Creates text file with the preprocessed text."""
        handle_text_dir("preprocess")

        preprocessed_text = preprocess(self.text)

        with open("preprocess/preprocessed_text.txt", "w", encoding="utf8") as output_file:
            output_file.write(preprocessed_text)

        message = (
            "\nYour text has now been preprocessed.\n"
            "You can use the other methods.\n"
            "If you find more noise, consider doing search and replace.\n"
            "In an editor like Libre Office Writer, Word, or Google Docs."
        )

        return message

    def get_word_list(self) -> None:
        """Creates text file with the word list."""
        word_list = make_word_list(self.text)

        with open("word_list.txt", "w", encoding="utf8") as output_file:
            output_file.write(word_list)

        return "\nYour word list has been saved in word_list.txt."


class App:
    """GUI Application for the Main class."""

    def __init__(self, root):
        self.root = root
        self.root.title("Text Processing Application")
        self.root.geometry("400x300")

        self.file_path = tk.StringVar()

        # Create input for file path
        self.file_entry = tk.Entry(root, textvariable=self.file_path, width=40)
        self.file_entry.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        # Create buttons for processing
        self.char_button = tk.Button(root, text="Generate Character List", command=self.generate_char_list)
        self.char_button.pack(pady=10)

        self.preprocess_button = tk.Button(root, text="Preprocess Text", command=self.preprocess_text)
        self.preprocess_button.pack(pady=10)

        self.word_button = tk.Button(root, text="Generate Word List", command=self.generate_word_list)
        self.word_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=20)

    def browse_file(self):
        """Open a file dialog to select a file."""
        file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_path.set(file_path)

    def load_main(self):
        """Initialize Main with the file path."""
        try:
            self.main = Main(self.file_path.get())
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def generate_char_list(self):
        """Handle character list generation."""
        self.load_main()
        try:
            message = self.main.get_char_list()
            messagebox.showinfo("Success", message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def preprocess_text(self):
        """Handle text preprocessing."""
        self.load_main()
        try:
            message = self.main.get_preprocessed_text()
            messagebox.showinfo("Success", message)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_word_list(self):
        """Handle word list generation."""
        self.load_main()
        try:
            message = self.main.get_word_list()
            messagebox.showinfo("Success", message)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
