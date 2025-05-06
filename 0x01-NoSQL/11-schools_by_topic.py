#!/usr/bin/env python3
"""module for task 11"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return [obj for obj in mongo_collection.find({'topics': topic})]
