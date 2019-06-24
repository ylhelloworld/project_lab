import pymongo

class MongoDocHelper(object):

    def __init__(self,db_name,collection_name):
        self.client = pymongo.MongoClient("mongodb://yang:yang#68@106.12.7.235:27017/admin")
        self.db = self.client[db_name]
        self.doc =self.db[collection_name]
 
    def insert(self,data):
        doc_info=dict(data)
        self.doc.insert(doc_info)
