import pymongo

class MongoHelper(object):

    def __init__(self,db_name,collection_name):
        client = pymongo.MongoClient("mongodb://yang:yang#68@106.12.7.235:27017/admin")
        db = client[db_name]
        self.doc = db[collection_name]

    def insert(self,data):
        doc_info=dict(data)
        self.doc.insert(doc_info)
