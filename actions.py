from handler import BaseMongoHandler


def save_collection(collection, data):
    db = BaseMongoHandler()
    result = db.save_objects_list(collection, data)
    return result


def save_object(collection, data):
	db = BaseMongoHandler()
	saved_object = db.save_single_object(collection, data)
	return save_object


def bulk_update(collection, query, data):
	db = BaseMongoHandler()
	saved_object = db.update_objects_list(collection, query, data)
	return save_object


def delete_object(collection, query):
	db = BaseMongoHandler()
	delete_result = db.delete_single_object()
	return delete_result


def search(collection, query={}, sort=None, limit=0):
	db = BaseMongoHandler()
	result = db.get_objects_list(collection, query, sort, limit)
	return result
