from lib.u_diary_entry import *
import pytest

"""
given invalid title and content type
raise type error
"""
def test_given_invalid_title_or_content_type_raise_type_error():
    with pytest.raises(TypeError) as err:
        UDiaryEntry(1,"12")
    error_message = str(err.value)
    assert error_message == "Invalid type, title and content must be string"

"""
given empty title and content
raise type error
"""
def test_given_empty_title_or_string_raise_error():
    with pytest.raises(Exception) as err:
        UDiaryEntry("", "hello world")
    error_message = str(err.value)
    assert error_message == "Title and content cannot be empty"

"""
given valid title and content
get the word count of the content
return an int that represents the amount of words in count 
"""
def test_given_valid_content_output_correct_word_count():
    obj_de = UDiaryEntry("first", "hello world! how is it going on this fine blue marble?")
    assert obj_de.count_words() == 11
"""
Given valid title, content and a wpm less than 1 
raise an exception
"""
def test_given_wpm_less_than_one_raise_error():
    obj_de = UDiaryEntry("first", "hello world")
    with pytest.raises(Exception) as err:
        obj_de.reading_time(-1)
    assert str(err.value) == "Error: wpm has to be 1 or higher"
    
"""
given valid title, content and wpm
get the reading time
return int that represents the time taken for the user to read the content
"""
def test_given_valid_content_output_correct_reading_time():
    obj_de = UDiaryEntry("first", "one two three four five six seven eight nine ten?")
    assert obj_de.reading_time(2) == 5
