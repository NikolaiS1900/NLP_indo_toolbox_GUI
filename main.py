"""Main module for running the program."""

from char_list import char_list
from load_file import load_file
from mk_text_dir import handle_text_dir
from preprocess import preprocess
from word_list import make_word_list

class Main:
    """Class for running the methods."""

    def __init__(self):
        self.text = load_file()

        handle_text_dir("text")

    def get_char_list(self) -> None:
        """Creates text file with the character list.

        It creates directory 'preprocess' if it doesn't exist.
        """

        handle_text_dir("preprocess")

        list_of_characters = char_list(self.text)

        with open("preprocess/character_to_delete.txt", "w", encoding="utf8") as output_file:
            output_file.write(list_of_characters)

        message = (
            "\nYour character list is ready and have been saved in character_list.txt.\n"
            "It is stored in the preprocess folder.\n"
            "Delete the characters you want to be removed from your text file."
            )

        print(message)

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
            "In a editor like Libre Office Writer, Word or Google Docs."
            )

        print(message)

    def get_word_list(self) -> None:
        """Creates text file with the word list."""

        word_list = make_word_list(self.text)

        with open("word_list.txt", "w", encoding="utf8") as output_file:
            output_file.write(word_list)


mii = Main()
mii.get_word_list()
