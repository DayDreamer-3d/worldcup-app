"""
Module contains all the locations data models
"""

import pydantic
import pydantic_mongo
import typing

from . import base
from ... import config


class Location(base.DataModel):  # pylint: disable=no-member
    
    lat: float = pydantic.Field(
        ge=-139.9604989,
        le=-73.6954839
    )
    lon: float = pydantic.Field(
        ge=15.8749696,
        le=54.6901083
    )


class Country(Location):
    """
    All WC host countries model.
    """

    id: typing.Literal[*config.COUNTRIES]


class City(Location):
    """
    All WC host cities model.
    """

    country: typing.Literal[*config.COUNTRIES]
    id: typing.Literal[*config.CITIES]


class Stadium(Location):
    """
    All WC host stadium model.
    """

    city: typing.Literal[*config.CITIES]
    id: typing.Literal[*config.STADIUMS]
    capacity: int = pydantic.Field(
        le=83264, ge=30000
    )

