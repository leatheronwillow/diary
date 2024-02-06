from lib.entry import Entry

"""
Given an entry with a title and contents
We see the title reflected back in the title property
We see the contents reflected back in the contents property
"""

def test_initialise_entry():
    entry = Entry("title", "contents")
    assert entry.title == "title"
    assert entry.contents == "contents"