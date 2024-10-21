"""Module to load the content of a text file."""

def load_file(file_path):
    """Load the content of the specified file."""

    if not file_path.endswith(".txt"):
        raise ValueError("\n\nThe file must be a .txt file.")
    else:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()