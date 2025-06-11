from lib.diary import *
import pytest
"""
Given zero entries 
get all
return empty list
"""
def test_given_zero_entry_all_outputs_empty_list():
    diary = Diary()
    assert diary.all() == []

"""
Given zero entries
get the count of words for all diary entries 
return number representing  number of words
"""
def test_given_zero_entry_ouput_zero_word_count():
    diary = Diary()
    assert diary.count_words() == 0

"""
Given zero entries
get the reading time for all diary entries 
raises exception
"""
def test_given_zero_entry_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(12)
    error_message = str(err.value)
    assert error_message == "No entries in diary. Unable to calculate reading time."


"""
Given zero entries
find best entry for reading time
raises exception
"""
def test_given_zero_entry_finding_best_entry_for_reading_time_raise_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(12,2)
    error_message = str(err.value)
    assert error_message == "No entries in diary. Unable to find best entry."
