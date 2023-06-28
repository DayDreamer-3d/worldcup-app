"""
Mongodb repo. for the location models.
"""

import typing

import pymongo
from pymongo import results

import pydantic_mongo

from . import base
from .. import models
from ... import config

# TODO: look for ways to change the base class dynamically
# so that we can use a single class from base.py to create
# multiple repos.


class Club(
    pydantic_mongo.AbstractRepository[models.Club]
):

    class Meta:
        collection_name = "clubs"


    def __init__(self, *args, **kwargs):

        client = pymongo.MongoClient(config.MONGO_URI)
        super().__init__(database=client.worldcup)
   
    # TODO: fix this method repeatition, have a base class ;(
    def save(
            self,
            new_model: typing.Any,
            old_model: typing.Any | None = None,
    ) -> typing.Union[
        results.InsertOneResult,
        results.UpdateResult
    ]:

        new_doc = self.to_document(new_model)
        
        if old_model:
            mongo_id = new_doc.pop("_id")
            return self.get_collection().update_one(
                {"_id": mongo_id}, {"$set": new_doc}
            )

        else:
            result = self.get_collection().insert_one(new_doc)
            new_model.id = result.inserted_id
            return result


class Nation(
    pydantic_mongo.AbstractRepository[models.Nation]
):

    class Meta:
        collection_name = "nations"


    def __init__(self, *args, **kwargs):

        client = pymongo.MongoClient(config.MONGO_URI)
        super().__init__(database=client.worldcup)
    
    def save(
            self,
            new_model: typing.Any,
            old_model: typing.Any | None = None,
    ) -> typing.Union[
        results.InsertOneResult,
        results.UpdateResult
    ]:

        new_doc = self.to_document(new_model)
        
        if old_model:
            mongo_id = new_doc.pop("_id")
            return self.get_collection().update_one(
                {"_id": mongo_id}, {"$set": new_doc}
            )

        else:
            result = self.get_collection().insert_one(new_doc)
            new_model.id = result.inserted_id
            return result


class Player(
    pydantic_mongo.AbstractRepository[models.Player]
):

    class Meta:
        collection_name = "players"

    def __init__(self, *args, **kwargs):

        client = pymongo.MongoClient(config.MONGO_URI)
        super().__init__(database=client.worldcup)
    
    def save(
            self,
            new_model: typing.Any,
            old_model: typing.Any | None = None,
    ) -> typing.Union[
        results.InsertOneResult,
        results.UpdateResult
    ]:

        new_doc = self.to_document(new_model)
        
        if old_model:
            mongo_id = new_doc.pop("_id")
            return self.get_collection().update_one(
                {"_id": mongo_id}, {"$set": new_doc}
            )

        else:
            result = self.get_collection().insert_one(new_doc)
            new_model.id = result.inserted_id
            return result

