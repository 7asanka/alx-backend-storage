#!/usr/bin/env python3
"""module for task 8"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
