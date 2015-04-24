import collections
from .internals.string_compat import is_str

def transform_keys(t, coll):
    """Recursively transforms all keys in coll with t. Does not modify coll."""
    if isinstance(coll, collections.MutableMapping):
        D = {}
        for k in coll:
            new_k = t(k) if is_str(k) else k
            D[new_k] = transform_keys(t, coll[k])
        return D
    elif is_str(coll):
        return coll
    elif isinstance(coll, collections.Iterable):
        return [transform_keys(t, x) for x in coll]
    else:
        return coll
