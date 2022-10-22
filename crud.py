from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib 
import pymongo 

# mongo_uri = "mongodb://username:" + urllib.parse.quote_plus("p@ssword") + "@localhost:35522"
# client = pymongo.MongoClient(mongo_uri)

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        # username = urllib.quote_plus('user')
        # password = urllib.quote_plus('pass/word')
        # self.client = MongoClient('mongodb://localhost:35522') 
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:35522/AAC' % (username, password))
        
        # where xxxx is your unique port number
        self.database = self.client['AAC']
        # self.database = self.client1['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            data_insert = self.database.animals.insert(data)
            if data_insert != 0:   
                return True# data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. 
    def read(self):
        data = self.database.animals.find({}) 
        return data
        #if data is not None:
            #self.database.animals.find(data)
            #return data
        #else:
            #return ("No data was found") 
        
    # The method to implement the U in CRUD.
    def update(self, data, new_data):
        if data is not None:
        # the save() method updates the document if this has an _id property 
            if data:
                saveResult = self.database.animals.update_one(data, new_data)
            return saveResult
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return False
            
# The method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            if data:
                removeResult = self.database.animals.delete_one(data)
        else:
           raise Exception("Nothing to delete, because data parameter is empty")
           return False