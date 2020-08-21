# isogonic-api
api for declination and isogonic lines using the WMM20 spherical harmonics model.

for an interactive visualisation of isogonic lines see the associated map: [https://isogonic-map.herokuapp.com/]

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
https://geomag-api.herokuapp.com/?lng=144.59537716183365&lat=-38.152063150975806&altitude_km=0&day=21&mth=8&yr=2020
https://geomag-api.herokuapp.com/isogon?yr=2020
```
## Deployment 

Use the poetry buildpack to deploy to heroku 
```
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
git push heroku master
```

## Reference:
See [https://www.ngdc.noaa.gov/geomag/WMM/]
