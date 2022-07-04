#!/usr/bin/env python3

from asyncio.windows_events import NULL


def list_all(mongo_collection):
    """ List all documents """
    lists = mongo_collection.find()
    if (lists.find() == NULL):
        return []
    else:
        return lists
        