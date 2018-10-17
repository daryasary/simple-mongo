class BaseMongoHandler:
	"""Base mongo transaction handler, all actions will be 
	implemented here"""
    
    def __init__(self, **kwargs):
        self.db = init_mongo(**kwargs)

	def get_collections_list(self):
        return self.db.collection_names()
