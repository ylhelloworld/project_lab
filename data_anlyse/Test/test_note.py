from Helper.mongo_helper import MongoHelper
import time
import tushare as ts
collect=MongoHelper('db','test')
collect.insert({'time':time.strftime('%Y-%m-%d %X', time.localtime())})
print('ok')
#time.strftime('%Y-%m-%d %X', time.localtime())
