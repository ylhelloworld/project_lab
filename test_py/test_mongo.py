from pymongo import MongoClient
print('start.......')

client=MongoClient('mongodb://yang:yang#68@106.12.7.235:27017/admin')
#db=client['test-database']
db=client.test
#collection=db['test-colleciton']
collection=db.test


data={'name':'yl','language':['C#','python']}

print(len(data))
post_id=collection.insert_one(data).inserted_id
print(post_id)