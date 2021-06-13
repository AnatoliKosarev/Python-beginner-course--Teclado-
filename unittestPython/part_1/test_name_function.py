import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):  # extends unittest.TestCase
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin", "ford")
        self.assertEqual(formatted_name, "Janis Ford Joplin")

    # if __name__ == "__main__":
    #     unittest.main()
