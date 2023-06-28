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


class Country(
    pydantic_mongo.AbstractRepository[models.Country]
):

    class Meta:
        collection_name = "countries"


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


class City(
    pydantic_mongo.AbstractRepository[models.City]
):

    class Meta:
        collection_name = "cities"


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


class Stadium(
    pydantic_mongo.AbstractRepository[models.Stadium]
):

    class Meta:
        collection_name = "stadiums"


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

