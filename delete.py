from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.EmployeeDb
def delete():
    try:

        criteria = input("\n Enter employee name to delete: ")

        db.Employees.delete_many({'name':criteria})
        print("\n Record deleted successfully \n")

    except Exception as e:
        print(str(e))
delete()