from .internals.misc import capitalize_http_header
from .internals.string_compat import lower, upper, capitalize
from .internals.decorator import conversion

def convert_case(first_fn, reset_fn, sep, s, **kwargs):
    """Converts the case of a string according to the rule for the first
       word, remaining words, and the separator.
    """
    return misc.convert_case(first_fn, rest_fn, sep, s, **kwargs)

CamelCase            = conversion("CamelCase", capitalize, capitalize, "")
PascalCase           = CamelCase
Camel_Snake_Case     = conversion("Camel_Snake_Case", capitalize,
                                  capitalize, "_")
camelCase            = conversion("camelCase", lower, capitalize, "")
SCREAMING_SNAKE_CASE = conversion("SCREAMING_SNAKE_CASE", upper, upper, "_")
snake_case           = conversion("snake_case", lower, lower, "_")
kebab_case           = conversion("kebab-case", lower, lower, "-")
HTTP_Header_Case     = conversion("HTTP-Header-Case", capitalize_http_header,
                                  capitalize_http_header, "-")
dot_case             = conversion("dot.case", lower, lower, ".")
Dot_Case             = conversion("Dot.Case", capitalize, capitalize, ".")
