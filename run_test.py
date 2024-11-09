import unittest
from logger import tk_handle_exception
from word_list import make_word_list


class TestModules(unittest.TestCase):
    def test1(self):
        """Test of tk_handle_exception on a GUI which raises an exception."""

        self.report_callback_exception = tk_handle_exception
        try:
            raise Exception("Test exception")
        except Exception as exception:
            tk_handle_exception(type(exception), exception, None)

    def test2(self) -> None:
        """Test make_word_list with empty string input.
        
        The empty string input should raise a ValueError.
        """
        input_text = ""
        
        with self.assertRaises(ValueError):
            make_word_list(input_text)

    def test3(self) -> None:
        """Test make_word_list with non-string input.
        
        The non-string input should raise a TypeError.
        """
        input_text = 123
        
        with self.assertRaises(TypeError):
            make_word_list(input_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
