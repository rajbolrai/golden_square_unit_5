from lib.todo_list import *
from lib.todo import *
import pytest

"""
Given single task to be added
get incomplete tasks
return the single task
"""
def test_added_single_task_then_get_incomplete_task_output_added_task():
    obj_todo_list = TodoList()
    obj_todo_1 = Todo("Rest well")
    obj_todo_list.add(obj_todo_1)
    assert obj_todo_list.incomplete() == [obj_todo_1]
    
"""
Added multiple tasks
get incomplete tasks
return a list with the all tasks added
"""
def test_added_multiple_tasks_then_get_incomplete_tasks_output_added_tasks():
    obj_todo_list = TodoList()
    obj_todo_1 = Todo("Rest well")
    obj_todo_2 = Todo("Recover well")
    obj_todo_3 = Todo("Heal well")
    obj_todo_4 = Todo("Power up")
    obj_todo_list.add(obj_todo_1)
    obj_todo_list.add(obj_todo_2)
    obj_todo_list.add(obj_todo_3)
    obj_todo_list.add(obj_todo_4)
    assert obj_todo_list.incomplete() == [obj_todo_1, obj_todo_2, obj_todo_3, obj_todo_4]
    
"""
Given a single task to add
give up and get complete task
return competed list with one task within it
"""
def test_added_single_task_then_give_up_and_get_completed_list_output_completed_list():
    obj_todo_list = TodoList()
    obj_todo_1 = Todo("Rest well")
    obj_todo_list.add(obj_todo_1)
    obj_todo_list.give_up()
    assert obj_todo_list.complete() == [obj_todo_1]

"""
Given a multiple tasks to add
give up and get complete list
return competed list with all tasks within it
"""
def test_added_multiple_tasks_then_give_up_and_get_complete_list_output_completd_list():
    obj_todo_list = TodoList()
    obj_todo_1 = Todo("Rest well")
    obj_todo_2 = Todo("Recover well")
    obj_todo_3 = Todo("Heal well")
    obj_todo_4 = Todo("Power up")
    obj_todo_list.add(obj_todo_1)
    obj_todo_list.add(obj_todo_2)
    obj_todo_list.add(obj_todo_3)
    obj_todo_list.add(obj_todo_4)
    obj_todo_list.give_up()
    assert obj_todo_list.complete() == [obj_todo_1, obj_todo_2, obj_todo_3, obj_todo_4]
    
"""
Added multiple tasks
give up and get incomplete task
return empty incomplete list
"""
def test_add_multiple_tasks_then_give_up_and_get_incomplete_list_output_empty_incomplete_list():
    obj_todo_list = TodoList()
    obj_todo_1 = Todo("Rest well")
    obj_todo_2 = Todo("Recover well")
    obj_todo_3 = Todo("Heal well")
    obj_todo_4 = Todo("Power up")
    obj_todo_list.add(obj_todo_1)
    obj_todo_list.add(obj_todo_2)
    obj_todo_list.add(obj_todo_3)
    obj_todo_list.add(obj_todo_4)
    obj_todo_list.give_up()
    assert obj_todo_list.incomplete() == []
    
""" 
Added multiple tasks and completed two
return the complete list with those two task in it    
"""
def test_added_tasks_completed_two_output_completed_list_with_two_completed_task():
    obj_todo_list = TodoList()
    obj_todo_1 = Todo("Rest well")
    obj_todo_2 = Todo("Recover well")
    obj_todo_3 = Todo("Heal well")
    obj_todo_4 = Todo("Power up")
    obj_todo_1.mark_complete()
    obj_todo_2.mark_complete()
    obj_todo_list.add(obj_todo_1)
    obj_todo_list.add(obj_todo_2)
    obj_todo_list.add(obj_todo_3)
    obj_todo_list.add(obj_todo_4)
    assert obj_todo_list.complete() == [obj_todo_1, obj_todo_2]
    
""" 
Added multiple tasks and completed two
return the complete list with those two task in it    
"""
def test_added_tasks_completed_two_output_incomplete_list_with_two_incompleted_task():
    obj_todo_list = TodoList()
    obj_todo_1 = Todo("one")
    obj_todo_2 = Todo("two")
    obj_todo_3 = Todo("three")
    obj_todo_4 = Todo("four")
    obj_todo_1.mark_complete()
    obj_todo_2.mark_complete()
    obj_todo_list.add(obj_todo_1)
    obj_todo_list.add(obj_todo_2)
    obj_todo_list.add(obj_todo_3)
    obj_todo_list.add(obj_todo_4)
    assert obj_todo_list.incomplete() == [obj_todo_3, obj_todo_4]
    