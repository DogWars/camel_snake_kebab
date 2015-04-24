import string
import sys

# In Python 3 the string module does not contain lower, upper,
# capitalize as functions anymore, but we need them.  So we define
# them here and bridge the differences (as far as camel_snake_kebab is
# concerned) between Python 2 and 3 in the process.

_is_py2 = sys.version_info[0] < 3
_strbase = basestring if _is_py2 else str

digits = set(string.digits)
whitespace = set(string.whitespace)
lowercase = set(string.ascii_lowercase)
uppercase = set(string.ascii_uppercase)

def lower(s):
    return s.lower()

def upper(s):
    return s.upper()

def capitalize(s):
    return s.capitalize()

def is_str(v):
    return isinstance(v, _strbase)
