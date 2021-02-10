from pymongo import MongoClient

class MongoAPI:
    def __init__(self,db_name,collection_name,db_ip='localhost',db_port=27017):
        self.db_name=db_name
        self.collection_name=collection_name
        self.db_ip=db_ip
        self.db_port=db_port
        self.client=MongoClient(host=self.db_ip,port=self.db_port)
        self.db=self.client[self.db_name]
        self.collection=self.db[self.collection_name]

    #增、查、删、改
    def insert(self,post_dic):
        self.collection.insert_one(post_dic)
    
    def get_one(self,query):
        return self.collection.find_one(query,projection={"_id":False})
    def get_all(self,query):
        return self.collection.find_all(query)
    def delete(self,query):
        return self.collection.delete_many(query)
    def update(self,query,post_dic):
        self.collection.update_one(
            query,
            {
                '$set':post_dic,
            },
            upsert=True
        )
    