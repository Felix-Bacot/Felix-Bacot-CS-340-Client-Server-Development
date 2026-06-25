# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d/%s' % (USER, PASS, HOST, PORT, DB)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
            
        if data is not None:
                    
            try:
                result = self.database.animals.insert_one(data)
                return result.acknowledged

            except Exception as e: 
                print("Insert error:", e)
                return False

            else: 
                return False 

    # Create method to implement the R in CRUD.
    def read(self, query):
        
        if query is not None:
            
            try:
                data = self.database.animals.find(query)
                return list(data)
            
            except Exception as e:
                print("Read error:", e)
                return []
            
            else:
                return []
    # creating an update method.        
            
    def update(self, query, new_values):
        
        if query is not None and new_values is not None:
            
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                
                return result.modified_count
            
            except Exception as e:
                print("Update error:", e)
                return 0
            
            return 0
        
    def delete(self, query):
            if query is not None:
                try:
                    
                    result = self.collection.delete_many(query)
                    return result.deleted_count
                
                except Exception as e:
                    print("Delete error:", e)
                    return 0
                
                
                return 0
        
       
            
            
            
            
        
    
                      
        

                         
     
           
        
 

            