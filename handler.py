class BaseMongoHandler:
	"""Base mongo transaction handler, all actions will be implemented here"""

    def __init__(self, **kwargs):
        self.db = init_mongo(**kwargs)

    def get_intended_scope(self, collection):
        return getattr(self.db, collection)

    def get_collections_list(self):
        return self.db.collection_names()

    def save_list(self, collection, data, force=True):
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
