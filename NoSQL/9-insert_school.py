#!/usr/bin/env python3
'''py function '''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''function than insert'''
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
