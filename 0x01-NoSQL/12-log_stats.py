#!/usr/bin/env python3
""" python script to fetch stats """
from pymongo import MongoClient

if __name__ == '__main__':
    """fetch specified stats """
    client = MongoClient()
    nginx = client.logs.nginx

    print(f'{nginx.count_documents({})} logs')

    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_checks = nginx.count_documents(
        {"path": "/status", "method": "GET"})
    print(f'{status_checks} status check')

    print('IPs:')
    ips = nginx.aggregate([{'$group': {'_id': '$ip',
                                       'count': {'$sum': 1}}},
                           {'$sort': {'count': -1}}, {'$limit': 10}])
    for ip in ips:
        print(f'\t{ip.get("_id")}: {ip.get("count")}')
