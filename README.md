# geomag-api
world magnetic model api for 2020 onwards.

for an interactive visualisation of values see the associated map: [https://geomag-map.herokuapp.com/]

Adapted from the geomagc software and World Magnetic Model of the NOAA
Satellite and Information Service, National Geophysical Data Center
http://www.ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml

Calculations forked from: [https://github.com/cmweiss/geomag/]

## Installation
```
poetry install
```

## Usage 

### Local

Run the server using 
```
python app/main.py
```

Using httpie [https://httpie.org/] submit requests as follows: 

Magnetic field values:

```
http GET :5002/ lat=-37.49 lng=144.58 altitude_km=0 day=14 mth=7 yr=2020
```

Yearly isogon files data (geojson) for the 1st of Jun:

```
http GET :5002/isogon yr=2020
```

### Live

```
http GET https://geomag-api.herokuapp.com/ lat=-37.49 lng=144.58 altitude_km=0 day=14 mth=7 yr=2020
http GET https://geomag-api.herokuapp.com/isogon yr=2020
```
## Deployment 

Use the poetry buildpack to deploy to heroku 
```
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
```

## Reference:
See [https://www.ngdc.noaa.gov/geomag/WMM/]
