from pymongo import MongoClient
from config import MONGO_URI

mongo_cli=MongoClient(MONGO_URI)
db=mongo_cli["media_bot"]
posts_collection=db["posts"]

def save_post(user_id,text=None,file_id=None):
  post_data={"user_id":user_id,"text":text,"file_id":file_id}
  posts_collection.insert_one(post_data)

def get_last_post(user_id):
  return
posts_collection.find_one({"user_id":user_id},sort=[("_id",-1)])
