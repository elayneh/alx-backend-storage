#!/usr/bin/env python3
""" update based on names """

import pymongo


def update_topics(mongo_collection, name, topics):
    """ updater based on specified name """
    mongo_collection.update({"name": name}, {"$set": {"topics": topics}})
    