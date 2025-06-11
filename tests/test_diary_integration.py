import pytest
from lib.diary import *
from lib.diary_entry import *
import pytest
"""
Add a single diary entry into diary
output list of single diary entry
"""
def test_adding_a_single_diary_entry_outputs_list_with_one_diary_entry():
    diary = Diary()
    d_entry_1 = DiaryEntry("first", "hello")
    diary.add(d_entry_1)
    assert diary.all() == [d_entry_1]

"""
add multiple diary entry into diary
output all entries as list
"""
def test_adding_multiple_diary_entries_output_list_with_multiple_diary_entries():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", "hello")
    d_entry_2 = DiaryEntry("2", "world!")
    d_entry_3 = DiaryEntry("3", "I have arrived")
    d_entry_4 = DiaryEntry("4", "boom!")
    diary.add(d_entry_1)
    diary.add(d_entry_2)
    diary.add(d_entry_3)
    diary.add(d_entry_4)
    assert diary.all() == [d_entry_1, d_entry_2, d_entry_3, d_entry_4]

"""
Given single diary entries
get the count of words for all diary entries 
return number representing  number of words
"""
def test_given_single_diary_entry_return_single_diary_entry__word_count():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", "one two three four five six seven eight nine ten")
    diary.add(d_entry_1)
    assert diary.count_words() == 10

"""
Given multiple diary entries
get the count of words for all diary entries 
return number representing  number of words
"""
def test_given_multiple_diary_entries_return_accumlated_word_count():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", "one two three four five six seven eight nine ten")
    d_entry_2 = DiaryEntry("2", """Lorem ipsum dolor sit amet, consectetuer adipiscing 
                        elit. Aenean commodo ligula eget dolor. Aenean massa. Can sociis 
                        natoque penatibus et!""")
    diary.add(d_entry_1)
    diary.add(d_entry_2)
    assert diary.count_words() == 30


"""
Given zero wpm and entries
get the reading time for all the entries
raises exception
"""
def test_given_zero_wpm_with_entries_raises_error():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", "one two three ")
    d_entry_2 = DiaryEntry("2", "one two three four")
    diary.add(d_entry_1)
    diary.add(d_entry_2)
    with pytest.raises(Exception) as err:
        diary.reading_time(0)
    error_message = str(err.value)
    assert error_message == "Error: wpm cannot be less than 1"


"""
Given two diary entry in diary and user's wpm
we try ascertain the time needed to read both
return user word per minute
"""
def test_given_two_diary_entries_output_reading_time():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", "one two three four five six seven eight nine ten")
    d_entry_2 = DiaryEntry("2", """Lorem ipsum dolor sit amet, consectetuer adipiscing 
                        elit. Aenean commodo ligula eget dolor. Aenean massa. Can sociis 
                        natoque penatibus et!""")
    d_entry_3 = DiaryEntry("3", """One morning, when Gregor Samsa woke from troubled dreams,
                        he found himself transformed in his bed into a horrible vermin.""")
    diary.add(d_entry_1)
    diary.add(d_entry_2)
    diary.add(d_entry_3)
    assert diary.reading_time(10) == 5

"""
Given word per minute, diary entries and minutes. 
find the best entry to read
return diary entry instance
"""
def test_given_multiple_entry_output_best_entry_for_reading_time():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", "one two three four five six seven eight nine ten")
    d_entry_2 = DiaryEntry("2", """Lorem ipsum dolor sit amet, consectetuer adipiscing 
                        elit. Aenean commodo ligula eget dolor. Aenean massa. Can sociis 
                        natoque penatibus et!""")
    d_entry_3 = DiaryEntry("3", """One morning, when Gregor Samsa woke from troubled dreams,
                        he found himself transformed in his""")
    diary.add(d_entry_1)
    diary.add(d_entry_2)
    diary.add(d_entry_3)
    assert diary.find_best_entry_for_reading_time(5, 3) == d_entry_3    

"""
Given word per minute, two same length diary entries and minutes. 
find the best entry to read
return first found diary entry instance
"""
def test_given_two_same_length_diary_entry_output_first_entry_for_best_reading_time():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", """Lorem ipsum dolor sit amet, consectetuer adipiscing 
                        elit. Aenean commodo ligula eget dolor. Aenean massa. Can sociis 
                        natoque penatibus et!""")
    d_entry_2 = DiaryEntry("2", """One morning, when Gregor Samsa woke from troubled dreams,
                        he found himself transformed in his bed into a horrible vermin.""")
    diary.add(d_entry_1)
    diary.add(d_entry_2)
    assert diary.find_best_entry_for_reading_time(5, 4) == d_entry_1                    

"""
Given a wpm and time that does provide enough time to read any entries. 
return string
"""
def test_given_long_diary_entry_and_slow_wpm_output_no_diary_entry():
    diary = Diary()
    d_entry_1 = DiaryEntry("1", """Lorem ipsum dolor sit amet, consectetuer adipiscing 
                        elit. Aenean commodo ligula eget dolor. Aenean massa. Can sociis 
                        natoque penatibus et!""")
    d_entry_2 = DiaryEntry("2", """One morning, when Gregor Samsa woke from troubled dreams,
                        he found himself transformed in his bed into a horrible vermin.""")
    d_entry_3 = DiaryEntry("3", "one two three four five six seven eight nine ten")
    diary.add(d_entry_1)
    diary.add(d_entry_2)
    diary.add(d_entry_3)
    assert diary.find_best_entry_for_reading_time(2, 3) == "Unable to read any entries within the given time"