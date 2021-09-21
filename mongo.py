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
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to MongoDB: %s") %e


conn = mongo_connect(MONGO_URI) #defines conn or connection

coll = conn[DATABASE] [COLLECTION] #defines the coll variable

coll.update_many({"nationality":"american"}, {"$set":{"hair-color":"maroon"}})

documents = coll.find({"nationality":"american"}) #returns all values from our mongo database as a MONGODB object

for doc in documents: #we need to iterate through this object
    print(doc) #and print it to test it


