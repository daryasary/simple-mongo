from handler import BaseMongoHandler


def save_collection(collection, data):
    db = BaseMongoHandler()
    result = db.save_list(collection, data)
    return result
