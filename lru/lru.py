"""
LRU (least recently used) cache implemented in python2 (OrderedDict is needed)

Initial testing:
import lru
cache = lru.LruCache(max_size=2)
cache.add('asdf_qwerty', '1q2w3e4r5t6y')
cache.add('qwerty', '1q2w3e4r5t6y')
cache.get('asdf_qwerty')
cache.add('ABC_123', '_3_XXX1q2w3e4r5t6y')

"""
from collections import OrderedDict


class CacheMiss(object):
    pass


class LruCache(object):
    """
    We are using OrderedDict so that we can say the closer to the start of the
    dictionary an enrtry is the further back in time it was used.
    So the closer to the end of the dictionary an entry is the more recently
    it was used.
    """

    def __init__(self, max_size=10):
        self._cache = OrderedDict()
        self._max_size = max_size

    def get(self, key):
        if key in self._cache:
            value = self._cache[key]
            # By adding it to the cache we ensure it's LRU order is updated
            self._add_entry(key, value)
        else:
            return CacheMiss
        return value

    def add(self, key, value):
        while len(self._cache) >= self._max_size:
            first_key = self._cache.keys()[0]
            del self._cache[first_key]
        self._add_entry(key, value)

    def _add_entry(self, key, value):
        if key in self._cache:
            del self._cache[key]
        # Add to end of ordered dictionary
        self._cache[key] = value
