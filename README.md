[![Build Status](https://travis-ci.org/kaelzhang/python-expire-cache.svg?branch=master)](https://travis-ci.org/kaelzhang/python-expire-cache)

# python-expirecache

A process-safe low-level python adapter to handle cache expiration.

## Install

```sh
$ pip install expirecache
```

## Usage

```py
from expirecache import Cache

ec = Cache(cache,
  load = None,
  allow_stale = True)

ec.set('my-key', 'blah-blah', expire = 60 * 60)
```

- **cache** the cache instance to be wrapped. It should contain 3 methods:
  - set `function(key, value)`
  - get `function(key)`
  - remove `function(key)`
- *load* `function(key)` method to load the new value of the key. When `ec.get(key)` is called, if the key is expired, expirecache will try use this method to load the new value, set the key, and returns the new value. During the loading process, a lock key will set the prevent other processes to load the 
- *allow_stale* `bool=True` by default, if a key has expired, we could still get the stale value of the key.

And then, one hour later:

```py
ec.get('my-key'); // 'blah-blah', it is stale, but we could still get it.
ec.has('my-key'); // False. Always use `ec.has()` to check if a key has expired.
```

#### ec.has(key)

Checks if the key is in the cache. If the key has expired, it will return `False`.

Always use this method to detect if the key is available.


#### ec.get(key)

Gets the value. If `allow_stale` is `True`, and the key has expired, this method would still get the old(stale) value of the key.

#### ec.set(key, value, expire = None)

- expire `int|None` the unit of `expire` is 'second'

Sets a value by key.


#### ec.remove(key)

Removes a key.

## License

MIT
