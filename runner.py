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
            abs(field(dlat, dlng, date=date)["D"]) # need to abs() to avoid singularity at +-180
            for dlng in y
        ]
        for dlat in x
    ]

    z = np.array(lookup)
    cs = plt.contour(
        y, x, z,
        levels=np.linspace(start=0, stop=180, num=180)
    )
    plt.savefig('plot.png')

    filename = "{}-{}-{}.json".format(day, mth, yr)
    geojson = geojsoncontour.contour_to_geojson(
        contour=cs,
        ndigits=3,
        unit='DD',
        geojson_filepath=filename
    )

    print("{} written".format(filename))

if __name__ == "__main__":
    bds = Bounds(90, -90, -180, 180)
    create_file(1, 1, 2020, bds)
