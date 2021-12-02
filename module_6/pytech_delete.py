import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.trf3y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

collection = db.students
students = collection

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

john = {
    "student_id": 1010,
    "first_name": "John",
    "last_name": "Doe"
}

john_student_id = students.insert_one(john).inserted_id

print("-- INSERT STATEMENT --")
print("Inserted student record into the students collection with student_id " + str(john_student_id) + "\n")

# adding new student and displaying
result = db.students.find_one({"student_id": 1010})
print("-- DISPLAYING STUDENT TEST DOC --")
print("Student ID: " + str(result["student_id"]))
print("First Name: " + result["first_name"])
print("Last Name: " + result["last_name"] + "\n")

# deleting newly added student
delete = db.students.delete_one({"student_id": 1010})

#result = db.students.delete_many({}) //this line is to delete all documents and start over

docs = db.students.find({})
print("-- DISPLAYING STUDENTS FROM find() QUERY --")
#i = 0 // for troubleshooting (keeping track of how many times the loop iterates)
for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
# // for troubleshooting (keeping track of how many times the loop iterates)
#    i = i + 1
#    print(i)
    print("\n")