import datetime
import json

import numpy as np

from geomag import field

if __name__ == "__main__":

    # creates a json grid file of magnetic field in geographic coords

    def create_json():

        date = datetime.date(year=2020, month=1, day=1)

        head = {
                "discipline": 10,
                "disciplineName": "Oceanographic_products",
                "center": -3,
                "centerName": "NOAA / British Geological Survey",
                "refTime": "{}T00:00:00.000Z".format(date),
                "significanceOfRT": 0,
                "significanceOfRTName": "Analysis",
                "parameterCategory": 1,
                "parameterCategoryName": "Currents",
                "parameterNumber": 2,
                "parameterNumberName": "U_component_of_current",
                "parameterUnit": "m.s-1",
                "forecastTime": 0,
                "surface1Type": 160,
                "surface1TypeName": "Depth below sea level",
                "surface1Value": 15,
                "numberPoints": 10000,
                "shape": 0,
                "shapeName": "Earth spherical with radius = 6,367,470 m",
                "scanMode": 0,
                "nx": 100,
                "ny": 100,
                "lo1": 0,
                "la1": 90,
                "lo2": 360,
                "la2": -90,
                "dx": 3.6,
                "dy": 1.8,
            }

        u = {"header": head, "data": []}
        v = {"header": head, "data": []}

        for dlat in np.linspace(
            start=head["la1"], stop=head["la2"], num=head["nx"]
        ):
            print("u : lat {}".format(dlat))
            for dlng in np.linspace(
                start=head["lo1"], stop=head["lo2"], num=head["ny"]
            ):

                vals = field(dlat, dlng, date=date)

                x = vals["X"] / 1
                u["data"].append(x)

                y = vals["Y"] / 1
                v["data"].append(y)

        to_dump = [v, u]

        filename = "{}-0000-wind-gfs-1.0.json".format(date.day)

        with open(filename, "w") as out:
            json.dump(to_dump, out)

        print("{} written".format(filename))

class Bounds: 
    def __init__(self, lat1, lat2, lng1, lng2):
        self.lat1 = lat1
        self.lat2 = lat2 
        self.lng1 = lng1
        self.lng2 = lng2

if __name__ == "__main__":
    create_json()
