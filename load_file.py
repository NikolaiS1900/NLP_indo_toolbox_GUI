"""This modulecontains a function for loading a text file."""

import glob
import sys

def load_file() -> str:
    """Checks the 'text' directory for a text file and read it.

    Thus function will only scan for files ending in .txt

    If there is more than one file, it will print a message and exit.

    If there is 0 files ending in .txt, it will print a message and exit.

    Returns: A variable containing the text from the file.
    """

    file_names = list(glob.glob("text/*.txt"))

    if len(file_names) == 0:
        print("No txt file found in text directory")
        sys.exit()
    if len(file_names) > 1:
        print("Multiple files found, can only handle one file at a time")
        sys.exit()

    if len(file_names) == 1:
        file = file_names[0]

        with open(file, "r", encoding="utf8") as found_file:
            read_text = found_file.read()

    return read_text
