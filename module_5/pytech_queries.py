import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.trf3y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

for doc in docs:
    print(doc)

doc = db.students.find_one({"student_id": 1007})

print(doc["student_id"])

