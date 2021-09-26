# Flask Project - Find Distance
### Flask Blueprint project to find the distance from the Moscow Ring Road to the specified address. 


# Setup

### Technologies used:

+ Python 3.6
+ Yandex-geocoder api
+ Geopy

You're advised to use venv from here on.

### Create virtual env:

python3 -m venv venv
. venv/bin/activate  # [.csh|.fish]

### install required packages
pip3 install -r requirements.txt

# Run Project

The address is passed to the application in an HTTP request, 
if the specified address is located inside the MKAD, the distance does not need to be calculated.

### Get distance

Send an GET request to the URL http://127.0.0.1:5000/calc_coordinates/ passing the address on request body
