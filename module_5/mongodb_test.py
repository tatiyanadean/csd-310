# Name:       Tatiyana Dean
# Assignment: Module 5.2
# Date:       11/15/21

import pymongo
from pymongo import MongoClient

url = "";
url = "mongodb+srv://admin:admin@cluster0.trf3y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

client = MongoClient(url)
db = client.pytech

print(db.list_collection_names())
