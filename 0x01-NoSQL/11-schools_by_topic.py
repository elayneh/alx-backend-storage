#!/usr/bin/env python3

""" Return documents from the collection """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Return schools with specified topic """
    # schools = []
    # if not mongo_collection:
    #     return schools
    return mongo_collection.find({}, {"topics": topic})
