import datetime
import json
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from geomag import WorldMagneticModel
from utils import contour_to_geojson


class Bounds: 
    def __init__(self, lat1, lat2, lng1, lng2):
        self.lat1 = lat1
        self.lat2 = lat2 
        self.lng1 = lng1
        self.lng2 = lng2

wmm = WorldMagneticModel()
def field(*args, **kwargs):
    return wmm.calc_field(*args, **kwargs).field

def create_file(day, mth, yr, bds):

    date = datetime.date(year=yr, month=mth, day=day)
    print('creating {}-{}-{}'.format(day, mth, yr))

    nx = 1000
    ny = 500

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
        levels=np.linspace(start=-180, stop=180, num=361)
    )
    # plt.savefig('plot.png')

    filename = "contour-plots/wmm-declination-contour-{}-{}-{}.json".format(day, mth, yr)
    geojson = contour_to_geojson(
        contour=cs,
        ndigits=3,
        unit='DD',
        geojson_filepath=filename
    )

    print("{} written".format(filename))

if __name__ == "__main__":

    bounds = Bounds(90, -89, -180, 180) 

    # create one plot per year
    for yr in np.linspace(start=2020, stop=2024, num=5):
        create_file(day=1, mth=6, yr=int(yr), bds=bounds)
