def bson2dict(data):
    if data:
        for k, v in data.items():
            if isinstance(v, ObjectId):
                data[k] = str(v)
        return data
    return {}