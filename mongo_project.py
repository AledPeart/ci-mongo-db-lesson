import os
import pymongo
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities" # theses 3 constant variables to make the code cleaner. Variable names are capitaised to show they are consts

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to MongoDB: %s") %e

def show_menu():
    print("") #this just prints a blank line to make it more visually appealing 
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option 

 #these variables catch the user inputs
def add_record():   
    print("")
    first = input("Enter first name > ")   
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

#new dictionary to be added, each value is now the variable that catches the user input
    new_doc = {   
            "first": first.lower(),
            "last": last.lower(),
            "dob": dob,
            "gender": gender,
            "hair_color": hair_color,
            "occupation": occupation,
            "nationality": nationality
            }
        
    try:
            coll.insert(new_doc)
            print("")
            print("Document inserted")
    except: 
            print("Error accessing the database")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
             print("invalid option")
        print("") #this just prints a blank line to make it more visually appealing


conn = mongo_connect(MONGO_URI) #defines conn or connection
coll = conn[DATABASE][COLLECTION] #defines the coll variable
main_loop()
            


