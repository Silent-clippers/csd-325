# Keanu Foltz CSD-325 12/1/24
# test the cities

import unittest
from city_functions import format_city_country

class test_city_functions(unittest.TestCase):
    def test_city_country(self):
        result = format_city_country('madrid', 'spain')
        self.assertEqual(result, 'Madrid, Spain')


if __name__ == '__main__':
    unittest.main()