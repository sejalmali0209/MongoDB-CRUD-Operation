from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.EmployeeDb

def read():
    try:
        empCol = db.Employee.find()
        print("\n All data from Employeedata database\n")
        for emp in empCol:
            print(emp)
    except Exception as e:
        print(str(e))
read()