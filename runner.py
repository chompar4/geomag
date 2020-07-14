import datetime
import json
from collections import defaultdict

import numpy as np

from geomag import field

if __name__ == "__main__":

    # creates a json grid file of magnetic field in geographic coords


    date = datetime.date(year=2020, month=1, day=1)

    nx = 360
    ny = 181

    lo1 = -179
    lo2 = 179
    la1 = 90
    la2 = -90

    x = np.linspace(start=la1, stop=la2, num=nx)
    y = np.linspace(start=lo1, stop=lo2, num=ny)

    lookup = []
    for dlat in x:
        print("u : lat {}".format(dlat))
        row = [
            field(dlat, dlng, date=date)["D"]
            for dlng in y
        ]
        lookup.append(row)


    import matplotlib.pyplot as plt
    z = np.array(lookup)
    cs = plt.contour(
        x, y,
        np.transpose(z),
        colors = 'black', 
        linestyles = 'dashed'
    )
    plt.clabel(cs, fmt = '%.0f', inline = True)
    plt.savefig('plot.png')

    # filename = "{}-0000-wind-gfs-1.0.json".format(date.day)

    # with open(filename, "w") as out:
    #     json.dump(to_dump, out)

    # print("{} written".format(filename))

class Bounds: 
    def __init__(self, lat1, lat2, lng1, lng2):
        self.lat1 = lat1
        self.lat2 = lat2 
        self.lng1 = lng1
        self.lng2 = lng2
