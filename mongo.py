from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.EmployeeDb

def insert():
    try:
        employeeid = input("Enter employee ID: ")
        employeeName = input("Enter employee name: ")
        employeeEmail = input("Enter employee email: ")
        employeeCountry = input("Enter employee country: ")
        employeeAge = input("Enter employee age: ")

        db.Employee.insert_one(
            {
                "id": employeeid,
                "name": employeeName,
                "email": employeeEmail,
                "country": employeeCountry,
                "age": employeeAge
            }
        )
        print("\n Insert Successful")
    except Exception as e:
        print(str(e))

insert()