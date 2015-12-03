#

import time

class Cache(object):
    """docstring for Cache
    """

    def __init__(self, cache,
                       load = None,
                       allow_stale = True):
        
        self.cache = cache;
        self.load = load;
        self.allow_stale = allow_stale;

    def get(self, key):
        value = 

    def _get(self, key):
        value = self.cache.get(key)
        if type(value) is tuple:
            return value
        return None

    def has(self, key):
        value = self._get(key)
        return self._has(value)

    def _has(self, value):
        if not value:
            return False

        if len(value) != 2:
            return False

        v, e = value

        # never expire
        if e == -1:
            return True

        ts = self._time()

        return ts < e

    def set(self, key, v, expire = None):
        if not expire:
            self.cache.set(key, (v, -1))
            return

        t = type(expire)
        if t is not float or t is not int:
            self.cache.set(key, (v, -1))
            return

        ts = self._time() + float(expire)
        self.cache.set(key, (v, ts))

    def remove(self, key):
        self.cache.remove(key)

    def _load(self, key):
        pass

    # method for testing
    def _time(self, key):
        return time.time()
    