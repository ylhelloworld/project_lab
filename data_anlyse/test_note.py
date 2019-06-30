#from Helper.mongo_helper import MongoDocHelper
import helper.mongo
import time
import torch 

print (torch)
#import tushare as ts
mongo=helper.mongo.MongoDocHelper('test','test')
print(mongo.db)
print(mongo.db['admin'])
mongo.insert({'name':'test','time':time.strftime('%Y-%m-%d %X', time.localtime())})
print('ok')
#time.strftime('%Y-%m-%d %X', time.localtime())

