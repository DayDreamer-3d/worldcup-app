"""
Responses related utilities
"""

import typing

import fastapi
from fastapi import status

from ... import config
from .. import models
from . import sequences


def error_response(
    verb: typing.Literal[*config.HTTP_VERBS.keys()],
    response: fastapi.Response,
    collection: str = "",
) -> tuple[fastapi.Response, models.Response]:

    error_info = config.HTTP_VERBS.get(
        verb, {
            status.HTTP_400_BAD_REQUEST:
            "Server can not process the request."
        }
    )

    code = list(error_info.keys())[0]
    message = eval(list(error_info.values())[0])

    response.status_code = code

    error = models.Error(code=code, message=message)
    custom_response = models.Response(error=error)

    return response, custom_response


def regular_response(
    # TODO: chec this : https://github.com/jefersondaniel/pydantic-mongo/blob/9c234d1fee8006bd846621840ed8d1851b2ac00d/pydantic_mongo/abstract_repository.py#L26
    # for generic type checking with a base class.
    items: dict[typing.Any, typing.Any]
) -> models.Response:

    return models.Response(**items)


def set_response(
    repo: typing.Any,
    items: list[typing.Any],
    verb: typing.Literal[*config.HTTP_VERBS.keys()],
    response: fastapi.Response,
    fields: list[str] = None,
) -> tuple[fastapi.Response, models.Response]:

    collection = repo.Meta.collection_name.lower()

    if items:
        custom_response = regular_response({collection: items})
    
    else:
        response, custom_response = error_response(
            verb, response, collection)
    
    return response, custom_response 

