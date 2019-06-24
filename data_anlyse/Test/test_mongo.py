from pymongo import MongoClient
print('start.......')

client=MongoClient('localhost',27017)
#db=client['test-database']
db=client.db1
#collection=db['test-colleciton']
collection=db.test


data={'name':'yl','language':['C#','python']}

print(len(data))
post_id=collection.insert_one(data).inserted_id
print(post_id)