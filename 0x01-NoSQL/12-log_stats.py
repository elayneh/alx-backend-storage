#!/usr/bin/env/ python3
"""  Python script that provides some stats about Nginx logs stored in MongoDB """

from tabnanny import check
from pymongo import MongoClient

if __name__ == "__main__":
    """ check presence of elements """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client["logs"]
    coll = db["nginx"]

    print(f"{coll.estimated_document_count()} logs")
    print("Methods:")
    for method in ["GET", "PUT", "POST", "PATCH", "DELETE"]:
        mc = coll.count_documents({"method": method})
        print("\tmethod {}: {}". format(method, mc))
    getter = coll.count_documents({
        'method': 'GET', 'path': "/status"
    })
    print("{} status check". format(getter))
