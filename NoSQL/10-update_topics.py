#!/usr/bin/env python3
'''py function '''
import pymongo


def update_topics(mongo_collection, name, topics):
    """update_topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
