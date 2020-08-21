from distutils.core import setup, find_packages

setup(
    name = 'isogonic-api',
    package = ['isogonic-api'],
    packages=find_packages("isogonic-api", exclude=["tests", "app", "isogons"])
    version = '1.0',
    description = 'magnetic field strength values and declination calculator',
    author = 'Sam Thompson',
    author_email = 'chompar4@gmail.com',
    url = 'https://github.com/chompar4/isogonic-api',
    download_url = 'https://github.com/chompar4/isogonic-api',
)