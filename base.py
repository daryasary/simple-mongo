import configs

from pymongo import MongoClient
from pymongo.errors import BulkWriteError, DuplicateKeyError


def init_mongo(**kwargs):
    """Init connection and authenticate if user credentials provided"""

    connection = MongoClient(configs.MONGO_HOST)
    mongo_db = connection[configs.MONGO_DB]
    if configs.MONGO_USER is not None:
        mongo_db.authenticate(configs.MONGO_USER, configs.MONGO_PASS)
    return mongo_db
