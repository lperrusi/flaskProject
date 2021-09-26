import unittest
from app.static import constants
from decimal import Decimal
from app.core.utils.coordinates_core import GeoCoder


class TestCoordinates(unittest.TestCase):
    def test_get_distance_value(self):
        """
        Test the get_distance param value
        :return:
        """
        geo_coder = GeoCoder()
        with self.assertRaises(ValueError):
            geo_coder.get_distance(1234)
            geo_coder.get_distance('Olinda')

    def test_check_address(self):
        """
        Test if the check address method is getting all coordinates from mkad_km constant
        :return:
        """
        geo_coder = GeoCoder()
        for coord in constants.mkad_km:
            address = (Decimal(coord[1]), Decimal(coord[2]))
            result = geo_coder.check_address(address, constants.mkad_km)
            self.assertEqual(result, True)
        address = (Decimal(constants.mkad_km[0][1]-1), Decimal(constants.mkad_km[0][2]-1))
        result = geo_coder.check_address(address, constants.mkad_km)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
