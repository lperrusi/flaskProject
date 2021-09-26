from typing import Tuple
from yandex_geocoder import Client as yandex_client
from app.static.constants import KEY, mkad_km
import geopy.distance
from decimal import Decimal
from typing import List, Union


class GeoCoder:

    def __init__(self):
        self.client = yandex_client(KEY)
        pass

    def get_distance(self, address: str):
        """
        Calculate the distance between the given address and the Moskow Ring Road
        :param address:
        :return: Distance between two address
        """
        coordinates_list = mkad_km
        moskow_coord = self.client.coordinates('Moscow Ring Road')
        address_coord = self.client.coordinates(address)
        check = self.check_address(address_coord, mkad_km)
        print(check)
        if check or address_coord == moskow_coord:
            return '200'
        else:
            distance = geopy.distance.distance(moskow_coord, address_coord).kilometers
            return distance

    @staticmethod
    def check_address(address, mkad: List[List[Union[int, float]]]):
        """
        Check if the address is inside the Moskow Ring Road
        :param address:
        :param mkad:
        :return:
        """
        try:
            for coordinate in mkad:
                if address == (Decimal(coordinate[1]), Decimal(coordinate[2])):
                    return True
                elif address == (Decimal('37.622289'), Decimal('55.705944')):
                    return True
            return False
        except:
            return "Wrong Params"
