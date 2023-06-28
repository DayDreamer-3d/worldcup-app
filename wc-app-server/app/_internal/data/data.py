"""
Module contains the data for the application
"""

from _impl import models


category1 = models.Category(
    name="category1",
    subcategorys=[
        models.SubCategory(name="subcategory1A"),
        models.SubCategory(name="subcategory1B"),
    ],
)

category2 = models.Category(
    name="category2",
    subcategorys=[
        models.SubCategory(name="subcategory2A"),
        models.SubCategory(name="subcategory2B"),
    ],
)

category3 = models.Category(name="category3")

categories = [category1, category2, category3]
