from lib.diary import *
from lib.diary_entry import *

"""
Add a single diary entry into diary
output list of single diary entry
"""
diary = Diary()
d_entry_1 = DiaryEntry("1", "hello")
diary.add(d_entry_1)
assert diary.all() == [['1', 'hello']]

"""
add multiple diary entry into diary
output all entries as list
"""
diary = Diary()
d_entry_1 = DiaryEntry("1", "hello")
d_entry_2 = DiaryEntry("2", "world!")
d_entry_3 = DiaryEntry("3", "I have arrived")
d_entry_4 = DiaryEntry("4", "boom!")
diary.add(d_entry_1)
diary.add(d_entry_2)
diary.add(d_entry_3)
diary.add(d_entry_4)
assert diary.all() == [
    ['1', 'hello'], ['2', 'world!'], 
    ['3', 'I have arrvied'], ['4', 'boom!']  
    ]

"""
Given two diary entry in diary and user's wpm
we try ascertain the time needed to read both
return user word per minute
"""
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