import pymongo

client = pymongo.MongoClient("mongodb://18.197.207.132:27017")

db = client['local']
print(db)
print(db.list_collection_names())
for i in db['alw_playaround'].find():
    print(type(i), i)
print('getting teststr', db['alw_playaround'].find_one({'test_str': 'this is a test string'}))
