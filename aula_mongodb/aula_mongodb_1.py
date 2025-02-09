from pymongo import MongoClient
import pprint
import datetime

try:
    cluster = MongoClient("mongodb://localhost:27017/")
    db = cluster['Databese']
    collection_ = db['Collection1']

    print(cluster)
    print(db)
    print(collection_)
    
    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }

    post_id = collection_.insert_one(post).inserted_id

    documentos = collection_.find()

    for doc in documentos:
        pprint.pprint(doc)

except:
    print('F')