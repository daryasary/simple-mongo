from utils import bson2dict


class BaseMongoHandler:
	"""Base mongo transaction handler, all actions will be implemented here"""

    def __init__(self, **kwargs):
        self.db = init_mongo(**kwargs)

    def get_intended_scope(self, collection):
        return getattr(self.db, collection)

    def get_collections_list(self):
        return self.db.collection_names()

    def get_objects_list(self, collection, query={}, sort=None, limit=0):
        intended = self.get_intended_scope(collection)
        if isinstance(query, dict):
            query = [query]

        if sort is None:
            result = intended.find(*query).limit(limit)

        else:
            result = intended.find(*query).sort(sort).limit(limit)

        return result, result.count()

    def get_single_object(self, collection, query={}):
        intended = self.get_intended_scope(collection)
        if isinstance(query, dict):
            query = [query]
        return bson2dict(intended.find_one(*query))

    def save_single_object(self, collection, data):
        intended = self.get_intended_scope(collection)
        inserted = intended.insert_one(data)
        return bson2dict(intended.find_one({'_id': inserted.inserted_id}))

    def save_objects_list(self, collection, data, force=True):
        intended = self.get_intended_scope(collection)

        try:
            inserted = intended.insert_many(data)
            ids = [str(i) for i in inserted.inserted_ids]
        except BulkWriteError:
            # This error means there is wrong item inside given list
            # if force is True objects should been saved separately 
            # one by one 
            ids = list()
            if force:
	            for d in data:
	                try:
	                    ids.append(str(intended.insert_one(d).inserted_id))
	                except DuplicateKeyError:
	                    # This dict is previously saved so continue for loop
	                    ids.append(str(intended.find_one(d)['_id']))
        return ids

    def update_objects_list(self, collection, query, data):
        intended = self.get_intended_scope(collection)
        updated = intended.update_many(query, data)
        return {
            "matched_count": updated.matched_count,
            "modified_count": updated.modified_count
        }

    def delete_single_object(self, collection, query):
        data = self.get_object(collection, query)
        intended = self.get_intended_scope(collection)
        return intended.delete_one(query)
