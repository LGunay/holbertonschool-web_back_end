#!/usr/bin/env python3
'''py function '''
import pymongo


def list_all(mongo_collection):
    '''function empty'''
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
