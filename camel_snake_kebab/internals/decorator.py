from .misc import convert_case

def conversion(name, first_fn, rest_fn, sep):
    def inner(s, **kwargs):
        return convert_case(first_fn, rest_fn, sep, s, **kwargs)
    inner.__doc__ = "Convert to " + name
    return inner
