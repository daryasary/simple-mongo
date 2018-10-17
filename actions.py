from handler import BaseMongoHandler


def save_collection(collection, data):
    db = BaseMongoHandler()
    result = db.save_objects_list(collection, data)
    return result

def save_object(collection, data):
	db = BaseMongoHandler()
	saved_object = db.save_single_object(collection, data)
	return save_object
