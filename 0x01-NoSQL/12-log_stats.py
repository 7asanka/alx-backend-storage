#!/usr/bin/env python3
"""module for task 12"""


from pymongo import MongoClient


def log_stats(nginx_collection):
    """script that provides some stats about Nginx logs stored in MongoDB"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """run log stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)


if __name__ == '__main__':
    run()
