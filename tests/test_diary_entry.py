from ast import AsyncFunctionDef
from os import error
from lib import diary_entry
from lib.diary import Diary
from lib.diary_entry import *
import pytest
"""
given invalid title and content type
raise type error
"""
def test_given_invalid_title_or_content_type_raise_type_error():
    with pytest.raises(TypeError) as err:
        DiaryEntry(1,"12")
    error_message = str(err.value)
    assert error_message == "Invalid type, title and content must be string"

"""
given empty title and content
raise type error
"""
def test_given_empty_title_or_string_raise_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "hello world")
    error_message = str(err.value)
    assert error_message == "Title and content cannot be empty"

"""
given valid title and content
get the word count of the content
return an int that represents the amount of words in count 
"""
def test_given_valid_content_output_correct_word_count():
    obj_de = DiaryEntry("first", "hello world! how is it going on this fine blue marble?")
    assert obj_de.count_words() == 11
"""
Given valid title, content and a wpm less than 1 
raise an exception
"""
def test_given_wpm_less_than_one_raise_error():
    obj_de = DiaryEntry("first", "hello world")
    with pytest.raises(Exception) as err:
        obj_de.reading_time(-1)
    error_message = str(err.value)
    assert error_message == "Error: wpm cannot be lower than 1"
    
"""
given valid title, content and wpm
get the reading time
return int that represents the time taken for the user to read the content
"""
def test_given_valid_content_output_correct_reading_time():
    obj_de = DiaryEntry("first", "one two three four five six seven eight nine ten?")
    assert obj_de.reading_time(2) == 5

"""
Given valid title, content, a wpm less than 1 and minute less than 1
raise an exception
"""
def test_given_wpm_and_minute_less_than_one_raise_error():
    obj_de = DiaryEntry("first", "hello world")
    with pytest.raises(Exception) as err:
        obj_de.reading_chunk(1, 0)
    error_message = str(err.value)
    assert error_message == "Error: wpm and minute cannot be lower than 1"

"""
Given valid title, content, wpm and minutes
Read one chunk of the content
return string that represents the chunk of content the user can read
"""
def test_reading_one_chunk_outputs_one_chunk_length_of_content():
    obj_de = DiaryEntry("first", "one two, three, four, five, six, seven, eight, nine, ten")
    assert obj_de.reading_chunk(3,2) == "one two three four five six"
    
"""
Given valid title, content, wpm and minutes
Read multiple chunks of the content
return string that represents current chunk of content the user can read
"""
def test_reading_multiple_chunk_outputs_one_chunk_length_of_content():
    obj_de = DiaryEntry("first", "one two, three, four, five, six, seven, eight, nine, ten")
    obj_de.reading_chunk(3,1)    
    obj_de.reading_chunk(1,3)    
    obj_de.reading_chunk(2,1)    
    assert obj_de.reading_chunk(2,1) == "nine ten"
    
"""
Given valid title, content, wpm and minutes
Read multiple large chunk of content and go over the length of content
return string that represents current chunk of content the user can read
"""
def test_reading_over_the_content_length_restarts_content_output():
    obj_de = DiaryEntry("first", "one two, three, four, five, six, seven, eight, nine, ten")
    obj_de.reading_chunk(3,2)    
    obj_de.reading_chunk(3,2)    
    assert obj_de.reading_chunk(2,1) == "one two"
    
def test_repr():
    obj_de = DiaryEntry("hello", "world")
    assert repr(obj_de) == 'hello'
    