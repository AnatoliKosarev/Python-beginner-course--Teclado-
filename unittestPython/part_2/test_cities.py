import unittest

from HelloWorld.unittestPython.part_2.cities_functions import get_formatted_city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for 'cities_functions.py'"""

    def test_country_city(self):
        formatted_result = get_formatted_city_country("chile", "santiago")
        self.assertEqual(formatted_result, "Santiago, Chile")

    def test_country_city_population(self):
        formatted_result = get_formatted_city_country("chile", "santiago", population=5000000)
        self.assertEqual(formatted_result, "Santiago, Chile - population 5000000")
