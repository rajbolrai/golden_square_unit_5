from lib.u_diary_entry import *
from lib.u_todo import *
from lib.user import *

"""
Add a single diary entry into diary
output list of single diary entry
"""
def test_read_diary_with_single_entry_outputs_one_entry():
    obj_user = User()
    obj_diary_entry = UDiaryEntry("thursday", "I will be working and resting")
    obj_user.add_diary_entry(obj_diary_entry)
    assert obj_user.read_diary() == [obj_diary_entry]

"""
Add a multiple diary entries into diary
output list of diary entries
"""
def test_read_diary_with_three_entries_outputs_three_entries():   
    obj_user = User()
    obj_diary_entry_1 = UDiaryEntry("thursday", "I will be working and resting")
    obj_diary_entry_2 = UDiaryEntry("fridday", "Work and rest")
    obj_diary_entry_3 = UDiaryEntry("Saturday", "Climbing and work")
    obj_user.add_diary_entry(obj_diary_entry_1)
    obj_user.add_diary_entry(obj_diary_entry_2)
    obj_user.add_diary_entry(obj_diary_entry_3)
    assert obj_user.read_diary() == [obj_diary_entry_1, obj_diary_entry_2, obj_diary_entry_3]

"""
Given a reading time that two entries are within the range of
return a list of 2 readable entries
"""
def test_get_two_readable_entries_within_reading_time():
    obj_user = User()
    obj_diary_entry_1 = UDiaryEntry("thursday", "I will be working and resting")
    obj_diary_entry_2 = UDiaryEntry("fridday", "Work and rest")
    obj_diary_entry_3 = UDiaryEntry("Saturday", "Climbing and work")
    obj_user.add_diary_entry(obj_diary_entry_1)
    obj_user.add_diary_entry(obj_diary_entry_2)
    obj_user.add_diary_entry(obj_diary_entry_3)
    assert obj_user.find_best_diary_entries_for_reading_time(4, 1) == [obj_diary_entry_2, obj_diary_entry_3]

"""
Given reading time less than what all entries require 
return empty list
"""
def test_get_no_entries_within_reading_time():
    obj_user = User()
    obj_diary_entry_1 = UDiaryEntry("thursday", "I will be working and resting")
    obj_diary_entry_2 = UDiaryEntry("fridday", "Work and rest")
    obj_diary_entry_3 = UDiaryEntry("Saturday", "Climbing and work")
    obj_user.add_diary_entry(obj_diary_entry_1)
    obj_user.add_diary_entry(obj_diary_entry_2)
    obj_user.add_diary_entry(obj_diary_entry_3)
    assert obj_user.find_best_diary_entries_for_reading_time(2, 1) == []

"""
Given single task to be added
get incomplete tasks
return the single task
"""
def test_get_one_incomplete_todo_task():
    obj_user = User()
    obj_todo = UTodo("watch a film")
    obj_user.add_todo_task(obj_todo)
    assert obj_user.todo_incomplete() == [obj_todo]

"""
Given single task to be added and complete it
get complete tasks
return the single task
"""
def test_get_one_complete_todo_task():
    obj_user = User()
    obj_todo = UTodo("watch a film")
    obj_todo.mark_complete()
    obj_user.add_todo_task(obj_todo)
    assert obj_user.todo_complete() == [obj_todo]

"""
Given four task to be added
complete two task 
return complete taks list with two task
"""
def test_get_two_incomplete_tasks():
    obj_user = User()
    obj_todo_1 = UTodo("watch a film")
    obj_todo_2 = UTodo("go walk")
    obj_todo_3 = UTodo("stretch well")
    obj_todo_4 = UTodo("drink water")
    obj_todo_4.mark_complete()
    obj_todo_3.mark_complete()
    obj_user.add_todo_task(obj_todo_1)
    obj_user.add_todo_task(obj_todo_2)
    obj_user.add_todo_task(obj_todo_3)
    obj_user.add_todo_task(obj_todo_4)
    assert obj_user.todo_complete() == [obj_todo_3, obj_todo_4]

"""
Given four task to be added
complete two task 
return incomplete taks list with two task
"""
def test_get_two_complete_tasks():
    obj_user = User()
    obj_todo_1 = UTodo("watch a film")
    obj_todo_2 = UTodo("go walk")
    obj_todo_3 = UTodo("stretch well")
    obj_todo_4 = UTodo("drink water")
    obj_todo_4.mark_complete()
    obj_todo_3.mark_complete()
    obj_user.add_todo_task(obj_todo_1)
    obj_user.add_todo_task(obj_todo_2)
    obj_user.add_todo_task(obj_todo_3)
    obj_user.add_todo_task(obj_todo_4)
    assert obj_user.todo_complete() == [obj_todo_3, obj_todo_4]

"""
Given diary entries
get mobile numbers from entries 
return list of mobile numbers
"""
def test_get_three_mobile_number_from_diary_entries():
    obj_user = User()
    obj_diary_entry_1 = UDiaryEntry("thursday", "I will be working and resting. 07000000001 07000000006 07000000001")
    obj_diary_entry_2 = UDiaryEntry("fridday", "Work and rest. 07000000002")
    obj_diary_entry_3 = UDiaryEntry("Saturday", "Climbing and work. 07000000003")
    obj_user.add_diary_entry(obj_diary_entry_1)
    obj_user.add_diary_entry(obj_diary_entry_2)
    obj_user.add_diary_entry(obj_diary_entry_3)
    assert obj_user.get_contacts() == ["07000000001", "07000000006", "07000000002", "07000000003"]
