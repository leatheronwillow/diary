from lib.diary import Diary
from lib.entry import Entry

"""
Given a diary
When we add two diary entries, they are reflected back in the entries list
"""
def test_add_entry_to_diary():
    diary = Diary()
    diary.add_entry("Title", "Contents")
    assert diary.entries[0].title == "Title"
    assert diary.entries[0].contents == "Contents"
    assert isinstance(diary.entries[0], Entry) == True

def test_read_diary_entry():
    diary = Diary()
    diary.add_entry("Title", "Contents")
    assert diary.read_entry("Title") == "Title: Contents"
    diary.add_entry("Heading", "Stuff")
    assert diary.read_entry("Heading") == "Heading: Stuff"