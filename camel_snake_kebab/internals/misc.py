from .string_separator import split, generic_separator
from .string_compat import capitalize, upper

def convert_case(first_fn, rest_fn, sep, s, separator=generic_separator):
    xs = split(separator, s)
    first = xs[0]
    rest = xs[1:]
    return sep.join([first_fn(first)] + [rest_fn(x) for x in rest])

_upper_case_http_headers = set(["CSP", "ATT", "WAP", "IP", "HTTP", "CPU", "DNT",
                                "SSL", "UA", "TE", "WWW", "XSS", "MD5"])

def capitalize_http_header(s):
    return upper(s) if s.upper() in _upper_case_http_headers else capitalize(s)
