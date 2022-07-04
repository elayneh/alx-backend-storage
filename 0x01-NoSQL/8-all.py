#!/usr/bin/env python3
""" mongo list """

import pymongo

def list_all(mongo_collection):
    """ List all documents """
    lists = mongo_collection.find()
    if not lists:
        return []
    else:
        return list(lists)
        