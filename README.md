# geomag
[![Build status](https://badge.buildkite.com/82cfc45a6dfec63cdf429b9e2b2037fe2416b3729d1db9aa94.svg)](https://buildkite.com/thompsonfilm/geomag)

api for declination and isogonic lines using the WMM20 spherical harmonics model.

to see isogonic lines view the live map: [https://isogonic-map.herokuapp.com/]

Adapted from the geomagc software and World Magnetic Model of the NOAA
Satellite and Information Service, National Geophysical Data Center
http://www.ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml

Calculations forked from: [https://github.com/cmweiss/geomag/]

## Installation
```
poetry install
```

### Live
```
https://isogonic-api.herokuapp.com/?lng=144.59537716183365&lat=-38.152063150975806&altitude_km=0&day=21&mth=8&yr=2020
https://isogonic-api.herokuapp.com/isogon?yr=2020
```
## Deployment 

Use the poetry buildpack to deploy to heroku 
```
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
git push heroku master
```

## Releases
To create a release use the command. If it complains you will need to ```pip install wheel``` first. 
```
python setup.py bdist_wheel
```


## Reference:
See [https://www.ngdc.noaa.gov/geomag/WMM/]
