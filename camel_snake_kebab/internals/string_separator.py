from . import string_compat as string
import re

RegexType = type(re.compile(""))

def split(other, s):
    if callable(other):
        return other(s)
    elif isinstance(other, RegexType):
        return re.split(other, s)
    else:
        return s.split(other)

_numbers = string.digits
_whitespace = string.whitespace.union({c for c in "-_."})
_lower = string.lowercase
_upper = string.uppercase

class Whitespace(object): pass
class Number(object): pass
class Lower(object): pass
class Upper(object): pass
class Other(object): pass

def classify_char(c):
    if c in _numbers:
        return Number
    elif c in _whitespace:
        return Whitespace
    elif c in _lower:
        return Lower
    elif c in _upper:
        return Upper
    else:
        return Other

def generic_split(ss):
    cs = [classify_char(s) for s in ss]
    result = []
    start = 0
    current = 0
    while True:
        next = current + 1
        if current >= len(ss):
            if current > start:
                result.append(ss[start:current])
                return result
            elif not result:
                # Return this instead of an empty list:
                return [""]
            else:
                return result
        elif cs[current] is Whitespace:
            if current > start:
                result.append(ss[start:current])
            start = next
        else:
            xs = cs[current:]
            a = xs[0] if len(xs) > 0 else None
            b = xs[1] if len(xs) > 1 else None
            c = xs[2] if len(xs) > 2 else None
            if (a is not Upper and b is Upper) \
              or (a is not Number and b is Number) \
              or (a is Upper and b is Upper and c is Lower):
                if next > start:
                    result.append(ss[start:next])
                start = next
        current = next

generic_separator = generic_split
