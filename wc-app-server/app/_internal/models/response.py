"""
Module contains all the rest api responses
"""

import fastapi
import pydantic
import typing

from . import locations, teams


class Link(pydantic.BaseModel):  # pylint: disable=no-member
    """
    Link Response class
    """
    rel: str
    href: str


class Error(pydantic.BaseModel):  # pylint: disable=no-member
    """
    Error model
    """
    code: str
    message: str


class Response(pydantic.BaseModel):  # pylint: disable=no-member
    """
    Class for all the responses
    """

    error: Error | None

    links: list[Link] = pydantic.Field(
        default=[],
        unique_items=True,
    )
    
    countries: list[locations.Country] = pydantic.Field(
        default=[],
        unique_items=True,
    )
    cities: list[locations.City] = pydantic.Field(
        default=[],
        unique_items=True,
    )
    stadiums: list[locations.Stadium] = pydantic.Field(
        default=[],
        unique_items=True,
    )

    nations: list[teams.Nation] = pydantic.Field(
        default=[],
        unique_items=True,
    )
    clubs: list[teams.Club] = pydantic.Field(
        default=[],
        unique_items=True,
    )
    players: list[teams.Player] = pydantic.Field(
        default=[],
        unique_items=True,
    )

    def dict(self, *args, **kwargs) -> dict:

        kwargs["exclude_unset"] = True
        kwargs["exclude_defaults"] = True
        kwargs["exclude_none"] = True

        return super().dict(*args, **kwargs)

        # ASK: how to condense the output to below type
        # TEST this with a egress model: {<name>: {<lat>, <lon>}}
