import hashlib

def hash_data(data: bytes):
    return hashlib.sha1(data).hexdigest()