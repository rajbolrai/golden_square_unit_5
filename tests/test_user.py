from lib.user import *
import pytest

"""
reading diary with no entries
return empty list
"""
def test_reading_diary_with_no_entries_return_empty_list():
    obj_user = User()
    assert obj_user.read_diary() == []
    
"""
Check type of wpm and minutes 
raise error if not int
"""
def test_given_invalid_wpm_and_minute_type_raise_type_error():
    obj_user = User()
    with pytest.raises(TypeError) as err:
        obj_user.find_best_diary_entries_for_reading_time("asfd", 2)
    assert str(err.value) == "Error: wpm and minute must be int"
    
"""
Check value of wpm and minutes 
raise error if less than 1
"""
def test_given_wpm_and_minute_less_than_1_raise_exception():
    obj_user = User()
    with pytest.raises(Exception) as err:
        obj_user.find_best_diary_entries_for_reading_time(0, -1)
    assert str(err.value) == "Error: wpm and minute must be greater than zero"