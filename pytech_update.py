import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.trf3y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})
print("-- DISPLAYING STUDENTS FROM find() QUERY --")
#i = 0
for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
#    i = i + 1
#    print(i)
    print("\n")

result = db.students.update_one(
    {
        "student_id": 1007
    }, 
    {
        "$set": 
        {
            "last_name": "Qinghua"
        }
    }
)

update = db.students.find_one({"student_id":1007})

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print("Student ID: " + str(update["student_id"]))
print("First Name: " + update["first_name"])
print("Last Name: " + update["last_name"])