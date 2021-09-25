from yandex_geocoder import Client as yandex_client
from static.constants import KEY, mkad_km
import geopy.distance
from decimal import Decimal

class GeoCoder:

    def __init__(self):
        self.client = yandex_client(KEY)
        pass

    def get_distance(self, address):
        """
        Calculate the distance between the given address and the Moskow Ring Road
        :param address:
        :return: Distance between two address
        """
        coordinates_list = mkad_km

        check = self.check_address(address, coordinates_list)

        if check:
            return '200'
        else:
            moskow_coord = self.client.coordinates('Moscow Ring Road')
            address_coord = self.client.coordinates(address)

            print(moskow_coord)
            print(address_coord)

            distance = geopy.distance.distance(moskow_coord, address_coord).kilometers
            return str(distance)

    @staticmethod
    def check_address(address, mkad):
        """
        Check if the address is inside the Moskow Ring Road
        :param address:
        :param mkad:
        :return:
        """
        for coordinate in mkad:
            if address[0] == coordinate[1] and address[1] == coordinate[2]:
                return True
        return False
