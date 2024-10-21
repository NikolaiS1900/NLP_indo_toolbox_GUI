import os
from gooey import Gooey, GooeyParser
from char_list import char_list
from load_file import load_file
from mk_text_dir import handle_text_dir
from preprocess import preprocess
from word_list import make_word_list

class Main:
    """Class for running the methods."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.text = load_file(file_path)
        self.file_name = os.path.basename(file_path)  # Get just the file name

    def get_char_list(self) -> None:
        """Creates a text file with the character list."""
        handle_text_dir("preprocess")  # Ensure 'preprocess' directory exists
        list_of_characters = char_list(self.text)

        file_name_no_white_space = self.file_name.replace(" ", "_")
        file_name_no_white_space_no_extension = file_name_no_white_space.replace(".txt", "")

        output_file_path = f"preprocess/{file_name_no_white_space_no_extension}_characters_to_delete.txt"
        with open(output_file_path, "w", encoding="utf8") as output_file:
            output_file.write(list_of_characters)

        message = (
            f"\nYou selected {self.file_name} to generate a character list from\n\n"
            f"Your character list is ready and has been saved in {output_file_path}.\n"
            "It is stored in the preprocess folder.\n"
            "Delete the characters you want to be removed from your text file."
        )
        print(message)  # This will now appear in the Gooey GUI output area

@Gooey(program_name="Text Processing Tool", 
       program_description="A simple tool to preprocess text files",
       default_size=(800, 600))
def main():
    parser = GooeyParser(description="Choose an action to perform")
    parser.add_argument('file_path', 
                        widget='FileChooser', 
                        help="Select the text file to process")
    
    # Action as a boolean flag
    parser.add_argument('--get_char_list', 
                        action="store_true", 
                        help="Generate a character list from the selected text file")

    args = parser.parse_args()

    # Initialize the Main class with the selected file path
    my_app = Main(args.file_path)

    # Perform the selected action
    if args.get_char_list:  # Check if the action flag is set
        print(args.get_char_list)  # This should now print in the GUI
        my_app.get_char_list()  # Call the method to get character list

if __name__ == "__main__":
    main()
