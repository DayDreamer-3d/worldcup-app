"""
Base models for the app.
"""

import bson
import pydantic
import pydantic_mongo


class DataModel(pydantic.BaseModel):
    """
    Base class for all data models.
    """

    # id: pydantic_mongo.ObjectIdField = None

    # class Config:
    #     json_encoders = {bson.ObjectId: str}

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __str__(self) -> str:
        cls_name: str = self.__class__.__name__
        return f"{cls_name}({self.name})"

