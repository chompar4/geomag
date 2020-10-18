from setuptools import find_packages, setup

AUTHOR = "Sam Thompson"
EMAIL = "chompar4@gmail.com"

requires = []
setup(
    name="geomag",
    version="8.0",
    author=AUTHOR,
    author_email=EMAIL,
    description="magnetic field strength values and declination calculator",
    install_requires=requires,
    packages=find_packages(),
    include_package_data=True,
)
