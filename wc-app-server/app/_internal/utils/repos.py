"""
Module containing repository related utilities.
"""

import typing

import fastapi
from fastapi import status

from ... import config
from .. import models
from . import responses


def _get_docs(
    # TODO: use Literal to strictly define this
    repo: typing.Any,
    q: dict[str, dict[str, str]] = None,

) -> list[typing.Any]:
    q = q or {}
    return list(repo.find_by(q))


def _set_doc(
    repo: typing.Any,
    new_item: typing.Any,
    old_item: str = None,

) -> list[typing.Any]:

    if old_item:  # update

        if new_item.id != old_item:
            _del_doc(repo, old_item)
            return _set_doc(repo, new_item)

    else:  # add

        if _get_docs(repo, {"id": new_item.id}):
            return []

    repo.save(new_item, old_item)
    items = [new_item] if new_item.id else []

    return items


def _del_doc(
    repo: typing.Any,
    item: str,

) -> list[typing.Any]:

    db_items = _get_docs(repo, {"id": item})
   
    if db_items:
        item = db_items[0]
        repo.delete(item)
        items = [item]

    else:
        items = []

    return items


def get_items(
    repo: typing.Any,
    response: fastapi.Response,
    q: dict[str, str] = None,
    fields: list = None,
    verb: typing.Literal[*config.HTTP_VERBS.keys()] = "GET",
) -> tuple[fastapi.Response, models.Response]:

    items = _get_docs(repo, q)
    return responses.set_response(repo, items, verb, response)


def save_item(
    repo: typing.Any,
    response: fastapi.Response,
    new_item: typing.Any,
    old_item: str = None,
    verb: typing.Literal[*config.HTTP_VERBS.keys()] = "POST",
) -> tuple[fastapi.Response, models.Response]:
    
    items = _set_doc(repo, new_item, old_item,)
    return responses.set_response(repo, items, verb, response)


def delete_item(
    repo: typing.Any,
    response: fastapi.Response,
    item: str,
    verb: typing.Literal[*config.HTTP_VERBS.keys()] = "DELETE",
) -> tuple[fastapi.Response, models.Response]:

    items = _del_doc(repo, item)
    return responses.set_response(repo, items, verb, response)
