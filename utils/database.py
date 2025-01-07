from .info import * 
from pymongo import MongoClient

dbclient = MongoClient(DATABASE_URI)
db       = dbclient["Auto-Delete"]
col      = db["DATA"]

def save_message(message, time):
    data = {"chat_id": message.chat.id,
            "message_id": message.id,
            "time": time}
    col.insert_one(data)
   
def get_all_data(time):
    data     = {"time":{"$lte":time}}
    all_data = list(col.find(data))
    return all_data

def delete_all_data(all_data):
    for data in all_data:
        col.delete_one(data)
