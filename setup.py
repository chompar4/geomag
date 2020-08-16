from distutils.core import setup, find_packages

setup(
    name = 'geomag',
    package = ['geomag'],
    packages=find_packages("geomag", exclude=["tests", "app", "contour-plots"])
    version = '1.0',
    description = 'earths magnetic field strength values and magnetic declination calculator',
    author = 'Sam Thompson',
    author_email = 'chompar4@gmail.com',
    url = 'https://github.com/chompar4/geomag_api',
    download_url = 'https://github.com/chompar4/geomag_api',
)