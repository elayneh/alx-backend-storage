#!/usr/bin/env python3
""" Insert document(s) in a given collection """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Inserts to school """
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
