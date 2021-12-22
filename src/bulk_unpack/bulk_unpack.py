def bulk_unpack(collection, keys, keep=True):
    for key in keys:
        yield collection[key] if keep else collection.pop(key)
