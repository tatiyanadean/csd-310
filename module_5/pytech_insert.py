import PyMongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.trf3y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

collection = db.students
students = collection

fred = {
    "student_id": 1007,
    "first_name": "Fred",
    "last_name": "Astaire"
}

bilbo = {
    "student_id": 1008,
    "first_name": "Bilbo",
    "last_name": "Baggins"
}

frodo = {
    "student_id": 1009,
    "first_name": Frodo,
    "last_name": Baggins
}

fred_student_id = students.insert_one(fred).inserted_id
bilbo_student_id = students.insert_one(bilbo).inserted_id
frodo_student_id = students.insert_one(frodo).inserted_id

print(fred_student_id)
print(bilbo_student_id)
print(frodo_student_id)
