import hashlib

_cache = {}

def cache_key(text):
    return hashlib.md5(text.encode()).hexdigest()

def get_cached(text):
    return _cache.get(cache_key(text))

def set_cache(text, value):
    _cache[cache_key(text)] = value