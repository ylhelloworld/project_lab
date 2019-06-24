#from Helper.mongo_helper import MongoDocHelper
import Helper.mongo_helper
import time
#import tushare as ts
mongo=Helper.mongo_helper.MongoDocHelper('test','test')
print(mongo.db)
print(mongo.db['admin'])
mongo.insert({'name':'test','time':time.strftime('%Y-%m-%d %X', time.localtime())})
print('ok')
#time.strftime('%Y-%m-%d %X', time.localtime())

