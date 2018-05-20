import pymongo

class MongoHelper(object):

    def __init__(self,db_name,collection_name):
        client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        db = client[db_name]
        self.doc = db[collection_name]

    def insert(self,data):
        doc_info=dict(data)
        self.doc.insert(doc_info)
