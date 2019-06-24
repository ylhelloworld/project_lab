from Helper.mongo_helper import MongoDocHelper
import time
#import tushare as ts
mongo=MongoDocHelper('test','test')
print(mongo.db)
print(mongo.db['admin'])
mongo.insert({'name':'test','time':time.strftime('%Y-%m-%d %X', time.localtime())})
print('ok')
#time.strftime('%Y-%m-%d %X', time.localtime())

