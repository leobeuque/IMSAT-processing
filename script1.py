# Based on laboratories write a script which:
#
#   - read a list of available Sentinel-2 images from the `Copernicus Open Access Hub`
#   - downloads from the `Copernicus Open Access Hub` the indicated image

## Imports
import sys
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
import geojson
from shapely import geometry
from sentinelsat import SentinelAPI
from datetime import date
import utm
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles
from ipyleaflet import Polygon as ipylPolygon

##getting arguments

switch = bool(sys.argv[1])
place_name = str(sys.argv[2])
uuid = str(sys.argv[3])
dir_address = str(sys.argv[4])
range = list(sys.argv[5])
cloudness = float(sys.argv[6]) # cloudcoverpercentage=(0, cloudness)

##Code

# address={'country':place_name[0],'city':place_name[1]}  # my cities
# geolocator = Nominatim(user_agent="Pio")
#
# location = geolocator.geocode(address)

print(5)