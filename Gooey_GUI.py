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
        print(message)

    def get_preprocessed_text(self) -> None:
        """Creates text file with the preprocessed text."""

        handle_text_dir("preprocess")

        file_name_no_white_space = self.file_name.replace(" ", "_")
        file_name_no_white_space_no_extension = file_name_no_white_space.replace(".txt", "")

        preprocessed_text = preprocess(self.text)

        with open(f"preprocess/{file_name_no_white_space_no_extension}_preprocessed_text.txt",
                  "w", encoding="utf8") as output_file:
            output_file.write(preprocessed_text)

        message = (
            "\nYour text has now been preprocessed.\n"
            f"It has been saved as {file_name_no_white_space_no_extension}_preprocessed_text.txt\n"
            "in the preprocess folder. You can use the other methods.\n"
            "If you find more noise, consider doing search and replace.\n"
            "In a editor like Libre Office Writer, Word or Google Docs."
            )

        print(message)

@Gooey(program_name="Text Processing Tool", 
       program_description="A simple tool to preprocess text files",
       default_size=(800, 600))
def main():
    parser = GooeyParser(description="Choose an action to perform")

    parser.add_argument('file_path', 
                        widget='FileChooser', 
                        help="Select the text file to process")
    
    # Action as a boolean flag
    
    parser.add_argument('--Option_menu_1', 
                    choices=['Get Character List', 'Preprocess Text', 'Get Word List'], 
                    help="Choose the action to perform on the text file")
    
    Extrator_group = parser.add_argument_group("Extrator_Options")
    
    # Add a text input field for the user to write a string
    Extrator_group.add_argument('--user_input_string', 
                       widget='TextField', 
                       help="Enter a custom string to print in the GUI")
    
    Extrator_group.add_argument("--inlaut", 
                       action='store_true', 
                       help="Make a search in inlaut (no regex)")

    args = parser.parse_args()

    # Initialize the Main class with the selected file path
    my_app = Main(args.file_path)

    # Perform the selected action
    if args.Option_menu_1 == 'Get Character List':
        my_app.get_char_list()
    if args.Option_menu_1 == 'Preprocess Text':
        my_app.get_preprocessed_text()
    if args.Option_menu_1 == 'Get Word List':
        my_app.get_word_list()
    # Print the custom string entered by the user, if provided
    if args.user_input_string:
        print(f"User Input: {args.user_input_string}")
    if args.inlaut:
        print("inlaut selected")


if __name__ == "__main__":
    main()
