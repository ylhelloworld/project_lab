from Helper.mongo_helper import MongoHelper
import time
#import tushare as ts
mongo=MongoHelper('test','test')
mongo.insert({'name':'test','time':time.strftime('%Y-%m-%d %X', time.localtime())})
print('ok')
#time.strftime('%Y-%m-%d %X', time.localtime())
