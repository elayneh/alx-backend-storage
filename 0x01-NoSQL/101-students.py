#!/usr/bin/env python3
""" Return sorted """
import pymongo


def top_students(mongo_collection):
    """ Returns list of students based ordered by score """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore":
                    {
                        "$avgscore": {
                            "$topics.score"
                        }
                    }
            }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
