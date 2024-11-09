import unittest
from logger import tk_handle_exception


class TestModules(unittest.TestCase):
    def test_logger(self):

        self.report_callback_exception = tk_handle_exception
        try:
            raise Exception("Test exception")
        except Exception as e:
            tk_handle_exception(type(e), e, None)


if __name__ == "__main__":
    unittest.main()
