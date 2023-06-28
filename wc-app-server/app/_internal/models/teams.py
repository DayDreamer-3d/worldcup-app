"""
Module contains all the teams data models.
"""

import datetime

import pydantic
import pydantic_mongo
import typing

from . import base
from ... import config


class Player(base.DataModel):

    id: str
    number: int
    position: typing.Literal[*config.POSITIONS]
    nation: str = pydantic.Field(hidden=True)
    club: str = pydantic.Field(hidden=True)
    birth: datetime.date

    @pydantic.validator("birth", pre=True)
    def birth_validate(cls, v):
        return datetime.date.fromisoformat(v)

    def dict(self: typing.Self, *args, **kwargs) -> dict:
        # TODO: rather than doing this
        # use egress class model to have 
        # fields which we want to expose
        result = super().dict()
        result["birth"] = str(result["birth"])
        return result



class Team(base.DataModel):  # pylint: disable=no-member
   
    id: str
    rank: int
    birth: int

    # @pydantic.validator("birth", pre=True)
    # def birth_validate(cls, v):
    #     return datetime.date.fromisoformat(v)

    # def dict(self: typing.Self, *args, **kwargs) -> dict:
    #     result = super().dict()
    #     result["birth"] = str(result["birth"])
    #     return result


class Nation(Team):
    """
    All WC player nations.
    """


class Club(Team):
    """
    All WC player clubs.
    """
