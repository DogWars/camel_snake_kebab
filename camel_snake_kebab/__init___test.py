# coding: utf-8
from . import *

def test_format_case_examples():
    assert 'fluxCapacitor' == camelCase("flux-capacitor")
    assert "I_AM_CONSTANT" == SCREAMING_SNAKE_CASE("I am constant")
    assert "object-id"     == kebab_case("object_id")
    assert "X-SSL-Cipher"  == HTTP_Header_Case("x-ssl-cipher")
    assert "s3_key"        == snake_case("s3-key", separator="-")
    assert "FooBar"        == CamelCase("FooBar")
    assert "FooBar"        == CamelCase("foo-bar")
    assert "FOO_BAR"       == SCREAMING_SNAKE_CASE("foo-bar")
    assert "foo-bar"       == kebab_case("foo bar")

def test_format_multiple():
    inputs = [
        "FooBar",
        "fooBar",
        "FOO_BAR",
        "foo_bar",
        "foo-bar",
        "Foo_Bar",
        "foo.bar",
        "Foo.Bar",
    ]
    functions = [CamelCase,
                 camelCase,
                 SCREAMING_SNAKE_CASE,
                 snake_case,
                 kebab_case,
                 Camel_Snake_Case,
                 dot_case,
                 Dot_Case]
    for input in inputs:
        for output, function in zip(inputs, functions):
            assert output == function(input)

def test_blank():
    assert "" == kebab_case("")
    assert "" == kebab_case(" ")

def test_http_header_case():
    cases = [
        ("User-Agent", "user-agent"),
        ("DNT", "dnt"),
        ("Remote-IP", "remote-ip"),
        ("TE", "te"),
        ("UA-CPU", "ua-cpu"),
        ("X-SSL-Cipher", "x-ssl-cipher"),
        ("X-WAP-Profile", "x-wap-profile"),
        ("X-XSS-Protection", "x-xss-protection"),
    ]
    for x, y in cases:
        assert x == HTTP_Header_Case(y)
