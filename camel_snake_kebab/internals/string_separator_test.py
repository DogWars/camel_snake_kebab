# coding: utf-8

from .string_separator import split, generic_separator
import re

def test_separators():
    regexp = re.compile(r"\.")
    assert ["foo", "bar"] == split(regexp, "foo.bar")
    assert [""] == split(regexp, "")

    assert ["foo", "bar"] == split(".", "foo.bar")
    assert [""] == split(".", "")

def test_generic_separator():
    f = lambda x: split(generic_separator, x)
    assert [""]                     == f("")
    assert [""]                     == f("   ")
    assert ["x"]                    == f(" x ")
    assert ["foo", "bar"]           == f("foo bar")
    assert ["foo", "bar"]           == f("foo\n\tbar")
    assert ["foo", "bar"]           == f("foo-bar")
    assert ["foo", "Bar"]           == f("fooBar")
    assert ["Foo", "Bar"]           == f("FooBar")
    assert ["foo", "bar"]           == f("foo_bar")
    assert ["FOO", "BAR"]           == f("FOO_BAR")

    assert ["räksmörgås"]           == f("räksmörgås")

    assert ["IP", "Address"]        == f("IPAddress")

    assert ["Adler", "32"]          == f("Adler32")
    assert ["Inet", "4", "Address"] == f("Inet4Address")
    assert ["Arc", "2", "D"]        == f("Arc2D")
    assert ["a", "123b"]            == f("a123b")
    assert ["A", "123", "B"]        == f("A123B")
