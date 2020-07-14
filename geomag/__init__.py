from .model import WorldMagneticModel

__all__ = ["WorldMagneticModel"]


def declination(*args, **kwargs):
    return WorldMagneticModel().calc_field(*args, **kwargs).declination


def field(*args, **kwargs):
    return WorldMagneticModel().calc_field(*args, **kwargs).field
