from config import db

movies_collection = db["movies"]

def add_movie(movie_data):
    return movies_collection.insert_one(movie_data)

def get_movies():
    return list(movies_collection.find({}))

def update_movie(movie_id, updated_data):
    return movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": updated_data})

def delete_movie(movie_id):
    return movies_collection.delete_one({"_id": ObjectId(movie_id)})
