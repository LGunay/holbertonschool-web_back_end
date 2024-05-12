#!/usr/bin/env python3
'''py function '''
import pymongo


def schools_by_topic(mongo_collection, topic):
    """schools topic"""
    return [i for i in mongo_collection.find({"topics": topic})]
