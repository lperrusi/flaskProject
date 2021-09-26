import logging
from . import main
from app.core.utils.coordinates_core import GeoCoder
from flask import request


@main.route("/calc_coordinates/")
def calc_coordinates():
    """

    :return:
    """
    logging.basicConfig(filename='std.log', filemode='w', level=logging.INFO)
    try:
        data = request.json
        geocoder = GeoCoder()
        result = geocoder.get_distance(data.get('address'))
        if type(result) == str:
            logging.info("Address is inside the Moskow Ring Road")
        else:
            logging.info("Distance %d km from the city %s to the Moskow Ring Road", result, data.get('address'))
        return '200'
    except:
        logging.warning('Wrong input address or input type')
        return "Wrong input address or input type"


