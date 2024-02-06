from lib.diary import Diary


"""
initialise diary
"""
def test_initialise_diary():
    diary = Diary()
    assert isinstance(diary, Diary) == True