import datetime
import json
from collections import defaultdict

import geojsoncontour
import matplotlib.pyplot as plt
import numpy as np

from geomag import field


class Bounds: 
    def __init__(self, lat1, lat2, lng1, lng2):
        self.lat1 = lat1
        self.lat2 = lat2 
        self.lng1 = lng1
        self.lng2 = lng2


def create_file(day, mth, yr, bds): 

    date = datetime.date(year=yr, month=mth, day=day)

    nx = 360
    ny = 181

    x = np.linspace(start=bds.lat1, stop=bds.lat2, num=nx)
    y = np.linspace(start=bds.lng1, stop=bds.lng2, num=ny)

    lookup = [
        [
            field(dlat, dlng, date=date)["D"]
            for dlng in y
        ]
        for dlat in x
    ]

    z = np.array(lookup)
    cs = plt.contour(
        y, x, z,
        levels=range(-180, 180, 2)
    )
    plt.savefig('plot.png')

    geojson = geojsoncontour.contour_to_geojson(
        contour=cs,
        ndigits=3,
        unit='DD'
    )

    filename = "{}-0000-wind-gfs-1.0.json".format(date.day)

    with open(filename, "w") as out:
        out.write(geojson)

    # print("{} written".format(filename))

class Bounds: 
    def __init__(self, lat1, lat2, lng1, lng2):
        self.lat1 = lat1
        self.lat2 = lat2 
        self.lng1 = lng1
        self.lng2 = lng2
