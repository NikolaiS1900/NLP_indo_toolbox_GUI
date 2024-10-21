import tkinter as tk
from tkinter import messagebox, filedialog
from char_list import char_list
from load_file import load_file
from mk_text_dir import handle_text_dir
from preprocess import preprocess
from word_list import make_word_list

class App:
    """GUI Application for text processing."""

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

    def load_file_content(self, file_path):
        """Load the content of the specified file."""
        if not file_path:
            raise ValueError("No file path provided.")
        return load_file(file_path)

    def generate_char_list(self):
        """Handle character list generation."""
        try:
            text = self.load_file_content(self.file_path.get())
            handle_text_dir("preprocess")  # Create the preprocess directory

            list_of_characters = char_list(text)

            with open("preprocess/character_to_delete.txt", "w", encoding="utf8") as output_file:
                output_file.write(list_of_characters)

            messagebox.showinfo("Success", "Character list has been saved in character_to_delete.txt in the preprocess folder.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def preprocess_text(self):
        """Handle text preprocessing."""
        try:
            # Open a new file selection dialog for preprocessing
            file_path = filedialog.askopenfilename(title="Select a Text File to Preprocess", filetypes=[("Text Files", "*.txt")])
            if not file_path:
                return  # If no file is selected, exit the method

            text = self.load_file_content(file_path)  # Load content from the selected file
            handle_text_dir("preprocess")  # Create the preprocess directory

            preprocessed_text = preprocess(text)

            with open("preprocess/preprocessed_text.txt", "w", encoding="utf8") as output_file:
                output_file.write(preprocessed_text)

            messagebox.showinfo("Success", "Text has been preprocessed and saved in preprocess/preprocessed_text.txt.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_word_list(self):
        """Handle word list generation."""
        try:
            text = self.load_file_content(self.file_path.get())
            word_list = make_word_list(text)

            with open("word_list.txt", "w", encoding="utf8") as output_file:
                output_file.write(word_list)

            messagebox.showinfo("Success", "Word list has been saved in word_list.txt.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
