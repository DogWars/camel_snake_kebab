from .extras import transform_keys
from . import kebab_case

def test_transform_keys():
    f = lambda x: transform_keys(kebab_case, x)
    assert None == f(None)
    assert {} == f({})
    assert [] == f([])
    assert {"total-books" : 0, "all-books" : []} \
        == f({"total_books" : 0, "allBooks" : []})
    assert [{"the-author" : "Dr. Seuss",
             "the-title"  : "Green Eggs and Ham"}] \
        == f([{"the-Author" : "Dr. Seuss", "The_Title" : "Green Eggs and Ham"}])
    assert {"total-books" : 1,
            "all-books"  : [{"the-author" : "Dr. Seuss",
                             "the-title"  : "Green Eggs and Ham"}]} \
        == f({"total_books" : 1,
              "allBooks"  : [{"THE_AUTHOR" : "Dr. Seuss",
                              "the_Title" : "Green Eggs and Ham"}]})
