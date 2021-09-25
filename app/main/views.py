from . import main
from app.utils.coordinates_core import GeoCoder
from flask import request


@main.route("/calc_coordinates/")
def calc_coordinates():
    """

    :return:
    """
    data = request.json
    geocoder = GeoCoder()
    return geocoder.get_distance(data.get('address'))
